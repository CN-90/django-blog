from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "Ilya-repin",
        "image": "02.jpg",
        "author": "Merlin the Wise",
        "date": date(2021, 6, 17),
        "title": "Ilya repin",
        "excerpt": "was a Ukrainian-born Russian Imperial realist painter. He was the most renowned Russian artists of the 19th century, when his position in the world of art was comparable to that of Leo Tolstoy in literature.",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ex, deserunt cupiditate, consequatur perferendis maiores est iure assumenda delectus natus praesentium eius necessitatibus totam tempora laborum similique sunt excepturi?
        """
    },
    {
        "slug": "William-Adolphe-Bouguereau",
        "image": "02.jpg",
        "author": "Merlin the Wise",
        "date": date(2021, 6, 17),
        "title": "William-Adolphe Bouguereau",
        "excerpt": "William-Adolphe Bouguereau (French pronunciation: ​[wiljam.adɔlf buɡ(ə)ʁo]; 30 November 1825 – 19 August 1905) was a French academic painter. In his realistic genre paintings he used mythological themes, making modern interpretations of classical subjects, with an emphasis on the female human body.[1] During his life, he enjoyed significant popularity in France and the United States, was given numerous official honors, and received top prices for his work.[2] As the quintessential salon painter of his generation, he was reviled by the Impressionist avant-garde.[2] By the early twentieth century, Bouguereau and his art fell out of favor with the public, due in part to changing tastes.[2] In the 1980s, a revival of interest in figure painting led to a rediscovery of Bouguereau and his work.[2] Throughout the course of his life, Bouguereau executed 822 known finished paintings, although the whereabouts of many are still unknown.[3]",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ex, deserunt cupiditate, consequatur perferendis maiores est iure assumenda delectus natus praesentium eius necessitatibus totam tempora laborum similique sunt excepturi?
        """
    },
    {
        "slug": "William-Adolphe-Bouguereau",
        "image": "02.jpg",
        "author": "Merlin the Wise",
        "date": date(2021, 6, 17),
        "title": "William-Adolphe Bouguereau",
        "excerpt": "William-Adolphe Bouguereau (French pronunciation: ​[wiljam.adɔlf buɡ(ə)ʁo]; 30 November 1825 – 19 August 1905) was a French academic painter. In his realistic genre paintings he used mythological themes, making modern interpretations of classical subjects, with an emphasis on the female human body.[1] During his life, he enjoyed significant popularity in France and the United States, was given numerous official honors, and received top prices for his work.[2] As the quintessential salon painter of his generation, he was reviled by the Impressionist avant-garde.[2] By the early twentieth century, Bouguereau and his art fell out of favor with the public, due in part to changing tastes.[2] In the 1980s, a revival of interest in figure painting led to a rediscovery of Bouguereau and his work.[2] Throughout the course of his life, Bouguereau executed 822 known finished paintings, although the whereabouts of many are still unknown.[3]",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ex, deserunt cupiditate, consequatur perferendis maiores est iure assumenda delectus natus praesentium eius necessitatibus totam tempora laborum similique sunt excepturi?
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
