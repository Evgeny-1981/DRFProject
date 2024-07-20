from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name="наименование")
    slug = models.CharField(max_length=120, verbose_name="слаг", unique=True)
    description = models.TextField(max_length=255, verbose_name="описание", **NULLABLE)
    image = models.ImageField(
        upload_to="media/course_image/", verbose_name="изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "course"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("name",)


class Lesson(models.Model):
    name = models.CharField(max_length=120, verbose_name="наименование")
    slug = models.CharField(max_length=120, verbose_name="слаг", unique=True)
    description = models.TextField(max_length=255, verbose_name="описание", **NULLABLE)
    image = models.ImageField(upload_to="media/lesson_image/", verbose_name="изображение", **NULLABLE)
    link_video = models.FileField(upload_to="media/lesson_video", verbose_name="видео", **NULLABLE)
    name_course = models.ForeignKey(Course, verbose_name="курс", related_name="урок", on_delete=models.CASCADE,
                                    **NULLABLE)

    def __str__(self):
        return f"Урок: {self.name} - курс {name_course}"

    class Meta:
        db_table = "lesson"
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("name", "name_course",)
