from ..loader import monkeypatch_schema
from ..skeleton import (AnnotationCollection, AnnotationPage, Canvas,
                        Collection, Manifest, Reference)


class ToReference:

    def to_reference(self):
        """Returns a Reference object that points to the calling object."""
        # Only try to set thumbnail if it's a Class that can have one
        if isinstance(self, (Collection, Manifest, Canvas)):
            thumbnail = self.thumbnail
        else:
            thumbnail = None

        # Currently the skeleton Reference requires a label, but some Referenceable objects may not have one (e.g AnnotationPage)
        # TODO: Remove this when the Schema is updated to have different reference types
        if not self.label:
            self.label = ""

        return Reference(id=self.id, label=self.label, type=self.type, thumbnail=thumbnail)


monkeypatch_schema([Manifest, AnnotationPage, Collection, AnnotationCollection, Canvas], ToReference)
