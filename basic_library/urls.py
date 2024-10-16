from rest_framework import routers

from basic_library.viewsets import ClientViewSet, AuthorViewSet, BookViewSet, GenreViewSet, LoanViewSet

router = routers.DefaultRouter()

router.register('client', ClientViewSet)
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)
router.register('genre', GenreViewSet)
router.register('loan', LoanViewSet)

urlpatterns = router.urls
