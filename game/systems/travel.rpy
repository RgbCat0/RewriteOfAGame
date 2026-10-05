# Map buttons and direct entry checks share the same travel restrictions.
init python:
    def map_entry_block_reason(destination):
        if destination in ("gotosunnyside", "overworldmap", "outsideoffice"):
            return None
        if headtosunnyside == 1:
            return "I should head to Sunnyside to pick up Mia and Katie."
        if headtooffice == 1:
            return "I should head to the office building in Sunnyside."
        if timeofday == "Night":
            if destination in ("malllabel", "mallstore"):
                return "The mall is closed at night."
            if destination in ("outsidegym", "gym"):
                return "The gym is closed at night."
            if destination == "school":
                return "I have no reason to go to school at night."
        return None

    def map_destination_action(destination):
        reason = map_entry_block_reason(destination)
        if reason is not None:
            return [SetVariable("_map_travel_message", reason), Jump("map_travel_denied")]
        return Jump(destination)

default _map_travel_message = ""

label map_travel_denied:
    # Keep the map background, but disable its buttons during the reminder.
    hide screen overworld
    hide screen overworldnight
    hide screen screen_sunnyside
    hide screen screen_sunnysidenight
    hide screen uppergui
    hide screen questboxpreview
    hide screen tosunnyside
    hide screen tonormalmap
    player "[_map_travel_message]"
    $ _map_travel_message = ""
    jump returnwhereyouare
