from pydantic import BaseModel
from typing import List, Literal, Optional

class ButtonStyles(BaseModel):
    size: Literal["Small", "Medium", "Large"] = "Medium"
    backgroundColor: Literal["Primary", "Secondary", "Success"] | str = "Primary"
    textColor: str = "#ffffff"  # Default to white text
    borderStyle: Literal["None", "Solid", "Dashed", "Dotted"] = "Solid"
    borderRadius: Literal["Rounded", "Rounded-XL", "Rounded-SM", "Rounded-MD", "Rounded-LG"] | int = "Rounded"
    fontWeight: Literal["Normal", "Bold"] = "Normal"
    fontSize: Optional[int] = None  # Allow users to optionally set font size

    def get(self) -> str:
        size_map = {
            "Small": "padding: 5px 10px; font-size: 12px;",
            "Medium": "padding: 10px 20px; font-size: 14px;",
            "Large": "padding: 15px 30px; font-size: 16px;",
        }

        background_color_map = {
            "Primary": "#007bff",
            "Secondary": "#6c757d",
            "Success": "#28a745",
        }

        border_radius_map = {
            "Rounded": "border-radius: 5px;",
            "Rounded-SM": "border-radius: 2px;",
            "Rounded-MD": "border-radius: 8px;",
            "Rounded-LG": "border-radius: 12px;",
            "Rounded-XL": "border-radius: 20px;",
        }

        background_color = background_color_map.get(self.backgroundColor, self.backgroundColor)
        border_radius = border_radius_map.get(self.borderRadius, f"border-radius: {self.borderRadius}px;") if isinstance(self.borderRadius, str) else f"border-radius: {self.borderRadius}px;"

        styles = f"""
            background-color: {background_color};
            color: {self.textColor};
            border: 2px {self.borderStyle.lower()} #dee2e6;
            {border_radius}
            font-weight: {self.fontWeight.lower()};
            {size_map[self.size]}
            cursor: pointer;
        """

        if self.fontSize:
            styles += f"font-size: {self.fontSize}px; "

        return " ".join(styles.split())  # Clean up whitespace for a tidier output
