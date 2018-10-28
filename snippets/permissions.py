from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    대상의 주인만 편집할수 있게 허가한다.
    """
    def has_object_permission(self, request, view, obj):
        # 읽는권한은 어떤요청에도 허가한다.
        # 우리는 GET, HEAD 그리고 OPTIONS requests를 허가한다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 snippet의 주인에게만 허락한다.
        return obj.owner == request.user
