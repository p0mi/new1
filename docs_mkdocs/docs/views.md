# Views

## UserListView

- **Класс**: `TemplateView`
- **Шаблон**: `'app/user_list.html'`
- **Метод**: `get_context_data`
  - **Описание**: Получает контекст для шаблона, включая записи пользователей из таблицы с указанным идентификатором.
  - **Действия**:
    1. Вызывается суперкласс для получения базового контекста.
    2. Использует функцию `get_users` для получения записей пользователей.
    3. В случае успешного получения записей, они добавляются в контекст.
    4. В случае ошибки возвращает пустой список.
    5. Контекст включает ключ `'records'`, содержащий записи пользователей.

---

## VirtualsListCreate

- **Класс**: `generics.ListCreateAPIView`
- **QuerySet**: `Virtuals.objects.all()`
- **Serializer Class**: `ItemSerializer`
- **Описание**: Представление для получения списка и создания объектов модели `Virtuals`.

---

## VitualsRetrieveUpdateDestroy

- **Класс**: `generics.RetrieveUpdateDestroyAPIView`
- **QuerySet**: `Virtuals.objects.all()`
- **Serializer Class**: `ItemSerializer`
- **Описание**: Представление для получения, обновления и удаления отдельных объектов модели `Virtuals`.

---