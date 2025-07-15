from django.shortcuts import render, redirect
from .models import Puzzle
import csv
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def dashboard(request):
    categories = ['Logical', 'Mathematical', 'Arrangement', 'Shape', 'Other']
    stats = {}
    puzzles_by_category = {}
    overall_solved = 0
    overall_total = 0
    for cat in categories:
        total = Puzzle.objects.filter(category=cat).count()  # type: ignore
        solved = Puzzle.objects.filter(category=cat, solved=True).count()  # type: ignore
        stats[cat] = {
            'solved': solved,
            'total': total,
            'percent': (solved / total * 100) if total > 0 else 0
        }
        puzzles_by_category[cat] = Puzzle.objects.filter(category=cat).order_by('title')  # type: ignore
        overall_solved += solved
        overall_total += total
    overall_percent = (overall_solved / overall_total * 100) if overall_total > 0 else 0
    return render(request, 'puzzles/dashboard.html', {
        'stats': stats,
        'puzzles_by_category': puzzles_by_category,
        'overall_solved': overall_solved,
        'overall_total': overall_total,
        'overall_percent': overall_percent,
    })

def puzzles_root_redirect(request):
    return redirect('dashboard')

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="puzzle_checklist.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Category', 'Asked In', 'Solved'])
    for puzzle in Puzzle.objects.all():  # type: ignore
        writer.writerow([puzzle.title, puzzle.category, puzzle.asked_in, 'Yes' if puzzle.solved else 'No'])
    return response

@csrf_exempt  # For simplicity; for production, use proper CSRF handling!
@require_POST
def toggle_solved(request):
    data = json.loads(request.body)
    puzzle_id = data.get('puzzle_id')
    solved = data.get('solved')
    try:
        puzzle = Puzzle.objects.get(id=puzzle_id)  # type: ignore
        puzzle.solved = solved
        puzzle.save()
        # Recalculate stats
        categories = ['Logical', 'Mathematical', 'Arrangement', 'Shape', 'Other']
        stats = {}
        for cat in categories:
            total = Puzzle.objects.filter(category=cat).count()  # type: ignore
            solved_count = Puzzle.objects.filter(category=cat, solved=True).count()  # type: ignore
            stats[cat] = {
                'solved': solved_count,
                'total': total,
                'percent': (solved_count / total * 100) if total > 0 else 0
            }
        overall_total = Puzzle.objects.count()  # type: ignore
        overall_solved = Puzzle.objects.filter(solved=True).count()  # type: ignore
        overall_percent = (overall_solved / overall_total * 100) if overall_total > 0 else 0
        return JsonResponse({'success': True, 'stats': stats, 'overall_percent': overall_percent})
    except Puzzle.DoesNotExist:  # type: ignore
        return JsonResponse({'success': False, 'error': 'Puzzle not found'}, status=404) 