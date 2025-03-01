# Models

## Roles

- **Role**: `models.TextChoices` (values: `'user'` -> 'User', `'admin'` -> 'Admin')

---

## Protocol

- **Protocol**: `models.TextChoices` (values: `'rdp'` -> 'RDP', `'ssh'` -> 'SSH', `'vnc'` -> 'VNC')

---

## Question

- **question_text**: `CharField` (max_length=200)
- **pub_date**: `DateTimeField` ("date published")

---

## Choice

- **question**: `ForeignKey` (to `Question`, on_delete=models.CASCADE)
- **choice_text**: `CharField` (max_length=200)
- **votes**: `IntegerField` (default=0)

---

## Virtuals

- **id**: `UUIDField` (primary_key=True, default=uuid.uuid4, editable=False)
- **hostname**: `CharField` (max_length=32)
- **protocol**: `CharField` (max_length=5, choices=Protocol.choices)
- **user_id**: `ForeignKey` (to `User`, on_delete=models.CASCADE)
- **address**: `CharField` (max_length=128)
- **port**: `IntegerField`
- **user_vm**: `CharField` (max_length=64)
- **password_vm**: `CharField` (max_length=128)
- **ignore_cert**: `BooleanField`

---

## Audit_log

- **id**: `UUIDField` (primary_key=True, default=uuid.uuid4, editable=False)
- **action**: `CharField` (max_length=32)
- **time**: `DateTimeField` (auto_now_add=True)
- **virtual_id**: `ForeignKey` (to `Virtuals`, on_delete=models.CASCADE)
- **user_id**: `ForeignKey` (to `User`, on_delete=models.CASCADE)

---