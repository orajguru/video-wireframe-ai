def generate_figma_json(components):

    figma_file = {
        "name": "AI Generated Wireframe",
        "type": "FRAME",
        "children": []
    }

    y = 0

    for comp in components:

        element = {
            "type": "RECTANGLE",
            "name": str(comp)[:40],
            "x": 0,
            "y": y,
            "width": 600,
            "height": 80
        }

        figma_file["children"].append(element)
        y += 100

    return figma_file