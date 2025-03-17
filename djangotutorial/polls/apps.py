from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PollsConfig(AppConfig):
    # Уникальное имя приложения
    name = 'polls'

    # Использование BigAutoField по умолчанию для автоинкрементируемых полей
    default_auto_field = 'django.db.models.BigAutoField'

    # Человекочитаемое имя приложения (используется в админке и других местах)
    verbose_name = _('Polls')

    def ready(self):
        """
        Метод ready вызывается один раз при запуске приложения.
        Здесь можно подключить сигналы, регистрировать фоновые задачи или выполнять другие инициализации.
        """
        # Импортируем сигналы, чтобы они были зарегистрированы
        try:
            import polls.signals  # Предполагается, что у вас есть файл signals.py
        except ImportError:
            pass

        # Пример регистрации фоновых задач (если используете Celery)
        # from .tasks import schedule_periodic_tasks
        # schedule_periodic_tasks()

        # Логирование инициализации приложения
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Приложение {self.name} успешно загружено.")