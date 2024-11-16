## Permissions and Groups in Bookshelf

This application uses Django's permissions and groups to manage access control.

### Permissions:
- `can_view`: Allows viewing book details.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

### Groups:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view book details.
- **Admins**: Have all permissions.

### Enforcing Permissions:
Permissions are enforced using the `@permission_required` decorator in views.
