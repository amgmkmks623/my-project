from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category

# 一覧
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all().order_by('is_done', 'id')
    return render(request, 'items/index.html', {
        'categories': categories,
        'items': items
    })

# 商品追加
def add_item(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        category_id = request.POST.get('category')
        memo = request.POST.get('memo', '')

        Item.objects.create(
            name=name,
            category_id=category_id,
            memo=memo
        )
        return redirect('index')

    return render(request, 'items/add.html', {'categories': categories})

# 商品削除
def delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('index')

# 完了切替
def toggle(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.is_done = not item.is_done
    item.save()
    return redirect('index')

# 商品編集
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        item.name = request.POST.get('name', '')
        item.category_id = request.POST.get('category')
        item.memo = request.POST.get('memo', '')
        item.save()
        return redirect('index')

    return render(request, 'items/edit.html', {
        'item': item,
        'categories': categories
    })

# カテゴリ追加
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        Category.objects.create(name=name)
        return redirect('index')

    return render(request, 'items/add_category.html')

# カテゴリ削除
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('index')

# カテゴリ編集
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.name = request.POST.get('name', '')
        category.save()
        return redirect('index')

    return render(request, 'items/edit_category.html', {
        'category': category
    })