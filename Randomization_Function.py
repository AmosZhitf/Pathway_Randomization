import numpy as np

def Pathway_Randomization(original_array, mode, sparsity=None, seed=None):
    """
    Shuffles the positions of ones in a matrix based on the chosen mode.

    Parameters:
        original_array (np.ndarray): The original matrix to be shuffled.
        mode (str): Shuffling mode ('row', 'column', 'global', 'sparsity').
        sparsity (float, optional): Sparsity threshold (only for 'sparsity' mode).
        seed (int, optional): Seed for reproducibility of random shuffling.

    Returns:
        np.ndarray: The shuffled matrix.
    """
    if mode not in ['row', 'column', 'global', 'sparsity']:
        raise ValueError("Invalid mode. Choose from 'row', 'column', 'global', or 'sparsity'.")

    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)

    new_array = np.zeros_like(original_array)

    if mode == 'column':
        # Keep the number of ones in each column constant
        for col in range(original_array.shape[1]):
            ones_indices = np.where(original_array[:, col] == 1)[0]
            zero_indices = np.where(original_array[:, col] == 0)[0]
            all_indices = np.concatenate((ones_indices, zero_indices))
            np.random.shuffle(all_indices)
            shuffled_column = np.zeros(original_array.shape[0], dtype=int)
            shuffled_column[all_indices[:len(ones_indices)]] = 1
            new_array[:, col] = shuffled_column

    elif mode == 'row':
        # Keep the number of ones in each row constant
        for row in range(original_array.shape[0]):
            ones_indices = np.where(original_array[row, :] == 1)[0]
            zero_indices = np.where(original_array[row, :] == 0)[0]
            all_indices = np.concatenate((ones_indices, zero_indices))
            np.random.shuffle(all_indices)
            shuffled_row = np.zeros(original_array.shape[1], dtype=int)
            shuffled_row[all_indices[:len(ones_indices)]] = 1
            new_array[row, :] = shuffled_row

    elif mode == 'global':
        # Keep the total number of ones constant
        total_ones = np.sum(original_array)
        flat_indices = np.arange(original_array.size)
        np.random.shuffle(flat_indices)
        ones_indices = flat_indices[:total_ones]
        np.put(new_array, ones_indices, 1)

    elif mode == 'sparsity':
        # Set the total number of ones based on the desired sparsity
        if sparsity is None:
            raise ValueError("For 'sparsity' mode, the 'sparsity' parameter must be specified.")
        total_elements = original_array.size
        total_ones = int(total_elements * (1 - sparsity))
        flat_indices = np.arange(total_elements)
        np.random.shuffle(flat_indices)
        ones_indices = flat_indices[:total_ones]
        np.put(new_array, ones_indices, 1)

    return new_array
