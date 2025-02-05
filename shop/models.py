import random
import string
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def rand_slug():
    """
    Return a random 3-character slug consisting of letters and digits.

    Returns:
        str: A random slug.
    """
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(3)
    )


class Category(models.Model):
    """
    Represents a category in the database.

    Attributes:
        name (CharField): The name of the category.
        parent (ForeignKey): The parent category, if any.
        slug (SlugField): The URL of the category.
        created_at (DateTimeField): The date the category was created.

    Notes:
        The parent category is a self-referential foreign key, allowing for a hierarchical category structure.
    """

    name = models.CharField("Категория", max_length=250, db_index=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        "URL", unique=True, max_length=250, null=False, editable=True
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        unique_together = (["slug", "parent"])
        verbose_name = "Категоря"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " -> ".join(full_path[::-1])

    def save(self, *args, **kwargs):
        """
        Saves the Category instance.

        If the slug is not set, generates a random slug using a combination of
        a random string, a fixed string '-pickBetter', and the category name.
        The slug is then slugified to ensure it is URL-friendly before saving
        the instance.

        """

        if not self.slug:
            self.slug = slugify(rand_slug() + "-pickBetter" + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:category-list", args=[str(self.slug)])


class Product(models.Model):
    """
    Represents a product in the database.

    Attributes:
        category (ForeignKey): Foreign key to the Category model.
        title (CharField): The title of the product.
        brand (CharField): The brand of the product.
        description (TextField): The description of the product.
        slug (SlugField): The URL of the product.
        price (DecimalField): The price of the product.
        image (ImageField): The image of the product.
        created_at (DateTimeField): The date the product was created.
        updated_at (DateTimeField): The date the product was last updated.
    """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    title = models.CharField("Название", max_length=250)
    brand = models.CharField("Бренд", max_length=250)
    description = models.TextField("Описание", max_length=250)
    slug = models.SlugField("URL", unique=True, max_length=250)
    price = models.DecimalField("Цена", max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField("Изображение", upload_to="products/%Y/%m/%d")
    available = models.BooleanField("Наличие", default=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[str(self.slug)])


class ProductManager(models.Manager):
    def get_queryset(self):
        """
        Return a queryset of available products by filtering the base queryset.

        Returns:
            QuerySet: A queryset of products that are available.
        """

        return super(ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True
