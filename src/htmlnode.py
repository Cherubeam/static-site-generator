class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children if children is not None else []
    self.props = props if props is not None else {}

  def __repr__(self):
    return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")

  def props_to_html(self):
    if self.props is None:
      return ""

    props_string = ""

    for key, value in self.props.items():
      props_string += f' {key}="{value}"'

    return props_string


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag=tag, value=value, children=None, props=props)

  def __repr__(self):
    return f"LeafNode(Tag: {self.tag}, Value: {self.value}, Props: {self.props})"
  
  def to_html(self):
    if not self.value:
      raise ValueError("No value for the tag provided")

    if not self.tag or self.tag == None:
      return self.value

    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag=tag, value=None, children=children, props=props)

  def __repr__(self):
    return f"ParentNode(Tag: {self.tag}, Children: {self.children}, Props: {self.props})"
  
  def to_html(self):
    if not self.tag:
      raise ValueError("No tag provided")

    if not self.children or self.children == []:
      raise ValueError("No children provided")

    children_html = ""
    for child in self.children:
      children_html += child.to_html()

    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"