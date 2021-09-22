from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Review
from .forms import AddCommentForm
from django.core.paginator import Paginator
from django.db.models import Avg

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'politicians/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'politicians/home.html'
    context_object_name = 'posts'
    ordering = ['name']
    paginate_by = 8

    def get_queryset(self):
        needs_rounding = Post.objects.annotate(avg_rating=Avg('comments__general_rate')).order_by('name')
        return needs_rounding

def post_detail_view(request, id):
    pk = id
    reviews = Review.objects.filter(person_id=id).order_by("-id")
    general_rating = reviews.aggregate(Avg("general_rate"))["general_rate__avg"]
    if(general_rating):
      general_rating = round(general_rating, 1)
    else:
      general_rating = " "
    honesty_rating = reviews.aggregate(Avg("honesty_rate"))["honesty_rate__avg"]
    if(honesty_rating):
      honesty_rating = round(honesty_rating, 1)
    else:
      honesty_rating = " "
    focus_rating = reviews.aggregate(Avg("focus_rate"))["focus_rate__avg"]
    if(focus_rating):
      focus_rating = round(focus_rating, 1)
    else:
      focus_rating = " "
    ambition_rating = reviews.aggregate(Avg("ambition_rate"))["ambition_rate__avg"]
    if(ambition_rating):
      ambition_rating = round(ambition_rating, 1)
    else:
      ambition_rating = " "
    respect_rating = reviews.aggregate(Avg("respect_rate"))["respect_rate__avg"]
    if(respect_rating):
      respect_rating = round(respect_rating, 1)
    else:
      respect_rating = " "
    persuasiveness_rating = reviews.aggregate(Avg("persuasiveness_rate"))["persuasiveness_rate__avg"]
    if(persuasiveness_rating):
      persuasiveness_rating = round(persuasiveness_rating, 1)
    else:
      persuasiveness_rating = " "
    commentsP = Paginator(reviews, 4)
    commentsPage = request.GET.get('page')
    commentsList = commentsP.get_page(commentsPage)
    context = {
        'object': Post.objects.get(id=id),
        'title': Post.objects.get(id=id).name,
        'reviews': reviews,
        'general_rating': general_rating,
        'honesty_rating': honesty_rating,
        'focus_rating': focus_rating,
        'ambition_rating': ambition_rating,
        'respect_rating': respect_rating,
        'persuasiveness_rating': persuasiveness_rating,
        'commentsList': commentsList
    }

    return render(request, "politicians/post_detail.html", context)

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = AddCommentForm
    template_name = 'politicians/add_comment.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.person_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('politician-detail', kwargs={'id': int(self.kwargs['pk'])})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Post.objects.filter(name__icontains=searched)
        ordered_venues = venues.order_by('name')
        ordered_posts = Post.objects.order_by('name')
        venueP = Paginator(ordered_venues, 8)
        venuePage = request.GET.get('page')
        venuesList = venueP.get_page(venuePage)

        return render(request, 'politicians/search_venues.html', {'searched': searched, 'venues': ordered_venues, 'title': searched, 'posts': ordered_posts, 'venuesList' : venuesList})
    else:
        postP = Paginator(Post.objects.all(), 8)
        postPage = request.GET.get('page')
        postsList = postP.get_page(postPage)
        context = {
            'posts': Post.objects.all(),
            'venuesList': postsList,
        }
        return render(request, 'politicians/search_venues.html', context)

def about(request):
    return render(request, 'politicians/about.html', {'title': 'შესახებ'})

def contact(request):
    return render(request, 'politicians/contact.html', {'title': 'კონტაქტი'})

def Review_rate(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        postz = Post.objects.get(id=prod_id)
        comment = request.GET.get('comment')
        honesty_rate = request.GET.get('honesty_rate')
        focus_rate = request.GET.get('focus_rate')
        ambition_rate = request.GET.get('ambition_rate')
        respect_rate = request.GET.get('respect_rate')
        persuasiveness_rate = request.GET.get('persuasiveness_rate')
        general_rate = request.GET.get('general_rate')
        user = request.user
        Review(user=user, postz=postz, comment=comment, honesty_rate=honesty_rate, focus_rate=focus_rate, ambition_rate=ambition_rate, respect_rate=respect_rate, persuasiveness_rate=persuasiveness_rate, general_rate=general_rate).save()
        return redirect('politician-detail', id=prod_id)