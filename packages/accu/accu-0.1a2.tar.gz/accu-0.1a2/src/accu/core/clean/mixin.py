from rest_framework import status
from rest_framework.response import Response

from accu.core.helpers.clean import remove_non_printable_characters, strip_html_tags


class CleanMixin:
    """Model mixin class which cleans inputs using the Mozilla bleach tools."""

    # Define a list of field names which will *not* be cleaned
    SAFE_FIELDS = []

    def create(self, request, *args, **kwargs):
        """Override to clean data before processing it."""
        serializer = self.get_serializer(data=self.clean_data(request.data))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """Override to clean data before processing it."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=self.clean_data(request.data), partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def clean_string(self, field: str, data: str) -> str:
        """Clean / sanitize a single input string.

        Note that this function will *allow* orphaned <>& characters,
        which would normally be escaped by bleach.

        Nominally, the only thing that will be "cleaned" will be HTML tags

        Ref: https://github.com/mozilla/bleach/issues/192
        """

        cleaned = strip_html_tags(data, field_name=field)
        cleaned = remove_non_printable_characters(cleaned)

        return cleaned

    def clean_data(self, data: dict) -> dict:
        """Clean / sanitize data.

        This uses mozillas bleach under the hood to disable certain html tags by
        encoding them - this leads to script tags etc. to not work.
        The results can be longer then the input; might make some character combinations
        `ugly`. Prevents XSS on the server-level.

        Args:
            data (dict): Data that should be sanatized.

        Returns:
            dict: Provided data sanatized; still in the same order.
        """

        clean_data = {}

        for k, v in data.items():

            if k in self.SAFE_FIELDS:
                ret = v
            elif isinstance(v, str):
                ret = self.clean_string(k, v)
            elif isinstance(v, dict):
                ret = self.clean_data(v)
            else:
                ret = v

            clean_data[k] = ret

        return clean_data
