import inkext
import xml.etree.ElementTree as ET

class HeadstoneDesigner(inkext.Extension):

  def __init__(self):
    # Extension information (mandatory)
    self.extension_id = "headstone_designer"
    self.extension_name = "Headstone Designer"

  def create_actions(self):
    # Define the "Create Headstone" action (mandatory)
    return [inkext.Action(
        id="create_headstone",
        name="Create Headstone",
        effects=inkext.Effect(
            proc=self.create_headstone,
            shortdesc="Creates a headstone based on user input",
        ),
        params=[
            # Define extension parameters (mandatory)
            inkext.Parameter(name="width", type=inkext.REAL, default=24, min=1, max=100),
            inkext.Parameter(name="height", type=inkext.REAL, default=36, min=1, max=100),
            inkext.Parameter(name="last_name", type=inkext.STRING, default=""),
            inkext.Parameter(name="first_middle_1", type=inkext.STRING, default=""),
            inkext.Parameter(name="first_middle_2", type=inkext.STRING, default=""),
            inkext.Parameter(name="dob_1", type=inkext.STRING, default=""),
            inkext.Parameter(name="dob_2", type=inkext.STRING, default=""),
            inkext.Parameter(name="dod_1", type=inkext.STRING, default=""),
            inkext.Parameter(name="dod_2", type=inkext.STRING, default=""),
            inkext.Parameter(name="text_height", type=inkext.REAL, default=1, min=0.5, max=5),
            inkext.Parameter(name="font_family", type=inkext.STRING, default="Verdana"),
        ]
    )]

  def create_headstone(self, node, width, height, last_name, first_middle_1, first_middle_2, dob_1, dob_2, dod_1, dod_2, text_height, font_family):
    # Access the Inkscape document (mandatory for modifying the document)
    document = self.document

    # Implement the logic for creating the headstone shape using Inkscape's path creation functions (replace with actual code)
    # ... (code to create headstone shape)

    # Helper function to create text element (similar to previous version)
    def create_text(text, x, y, anchor, font_size, font_family):
      text_element = ET.Element("text", transform=f"translate({x},{y})")
      text_element.text = text
      text_element.set("style", f"font-size:{font_size}px;font-family:{font_family}")
      text_element.set("text-anchor", anchor)
      return text_element

    # Calculate positions for text elements based on headstone dimensions and text size
    last_name_y = height * 0.7  # Adjust position as needed
    first_middle_y = height * 0.5  # Adjust position as needed
    dates_y = height * 0.2  # Adjust position as needed

    # Create text elements and add them to the document layer
    layer = document.get_current_layer()
    layer.append(create_text(last_name, width / 2, last_name_y, "middle", text_height, font_family))
    full_name = f"{first_middle_1} {first_middle_2}"
    if full_name:
      layer.append(create_text(full_name, width / 2, first_middle_y, "middle", text_height, font_family))

    # Create text elements for dates (assuming two lines)
    dob_text = f"{dob_1} {dob_2}"
    dod_text = f"{dod_1} {dod_2}"
    layer.append(create_text(dob_text, width / 2, dates_y, "middle", text_height, font_family))
