#
#  PriorityToColourTransformer.py
#  ToDos
#
#  Converted by u.fiedler on 09.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Cocoa import NSColor, NSValueTransformer


class PriorityToColourTransformer(NSValueTransformer):
    @classmethod
    def transformedValueClass(cls):
        return NSColor

    @classmethod
    def allowsReverseTransformation(cls):
        return False

    def transformedValue_(self, priority):
        if priority is None:
            return NSColor.blackColor()
        elif priority > 4:
            return NSColor.redColor()
        elif priority > 3:
            return NSColor.orangeColor()
        elif priority > 2:
            return NSColor.blueColor()
        elif priority > 1:
            return NSColor.greenColor()
        elif priority > 0:
            return NSColor.brownColor()
        else:
            return NSColor.blackColor()
