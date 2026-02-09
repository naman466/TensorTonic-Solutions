def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    H = len(image)
    W = len(image[0])

    cy = (H - 1) / 2.0
    cx = (W - 1) / 2.0

    theta = math.radians(angle_degrees)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    out = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            # offset from center
            dy = i - cy
            dx = j - cx

            # inverse rotation mapping
            src_y = cy + dy * cos_t + dx * sin_t
            src_x = cx - dy * sin_t + dx * cos_t

            # nearest neighbor
            src_y_round = int(round(src_y))
            src_x_round = int(round(src_x))

            # check bounds
            if 0 <= src_y_round < H and 0 <= src_x_round < W:
                out[i][j] = image[src_y_round][src_x_round]
            else:
                out[i][j] = 0

    return out