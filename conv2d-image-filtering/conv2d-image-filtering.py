def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """

    H = len(image)
    W = len(image[0])
    kH = len(kernel)
    kW = len(kernel[0])

    # create padded image
    if padding > 0:
        padded = [[0]*(W + 2*padding) for _ in range(H + 2*padding)]
        for i in range(H):
            for j in range(W):
                padded[i + padding][j + padding] = image[i][j]
    else:
        padded = image

    H_p = len(padded)
    W_p = len(padded[0])

    # output dimensions
    out_H = (H_p - kH) // stride + 1
    out_W = (W_p - kW) // stride + 1

    output = [[0 for _ in range(out_W)] for _ in range(out_H)]

    # convolution
    for i in range(out_H):
        for j in range(out_W):
            s = 0
            for ki in range(kH):
                for kj in range(kW):
                    s += padded[i*stride + ki][j*stride + kj] * kernel[ki][kj]
            output[i][j] = s

    return output