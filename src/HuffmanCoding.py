
import sys
import heapq


def Huffman_Map(huffman_tree, huffman_map=dict(), var=''):
    if (len(huffman_tree) == 1):
        label, freq = huffman_tree[0]
        huffman_map[label] = var

    else:
        value, node1, node2 = huffman_tree
        Huffman_Map(node1, huffman_map, var + "0")
        Huffman_Map(node2, huffman_map, var + "1")

    return huffman_map


def Frequency_Tree(frequency):
    Frequency_heap_tree_list = []
    for leaf_frequency in\
    frequency:heapq.heappush(Frequency_heap_tree_list, [leaf_frequency])
    while (len(Frequency_heap_tree_list) > 1):
        node1 = heapq.heappop(Frequency_heap_tree_list)
        node2 = heapq.heappop(Frequency_heap_tree_list)
        frequency_0, label_0 = node1[0]
        frequency_1, label_1 = node2[0]
        var1 = frequency_0 + frequency_1, label_0 + label_1
        Huffman_node = [(var1), node1, node2]
        heapq.heappush(Frequency_heap_tree_list, Huffman_node)
    return Frequency_heap_tree_list.pop()


def Freqency_of_char(info):
    characters = dict()
    for character in info:
        if not characters.get(character):
            characters[character] = 1
        else:
            characters[character] += 1
    return characters.items()


def huffman_encoding(info):
    if info is None or info == '':
        print("Unable to encode \n Error:Empty input detected")
        return '', None
    huffman_tree = Frequency_Tree(Freqency_of_char(info))
    huffman_map = Huffman_Map(huffman_tree)
    info = "".join([huffman_map[character] for character in info])
    return info, huffman_tree


def huffman_decoding(info, huffman_tree):
    if info is None or info == '':
        print("Unable to decode \n Error:Empty input detected")
        return None
    Tree_element = huffman_tree
    huffmaan_letters_decoded = []

    for char in info:
        if (char is '1'):
            Tree_element = Tree_element[2]
        else:
            Tree_element = Tree_element[1]

        if (len(Tree_element) == 1):
            label, freq = Tree_element[0]
            huffmaan_letters_decoded .append(label)
            Tree_element = huffman_tree

    return "".join(huffmaan_letters_decoded)


if __name__ == "__main__":
    codes = {}
    # Edge case
    a_great_sentence = ""
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    print(encoded_data, tree)
    print(decoded_data)

    # test case 1
    a_great_sentence = "The bird is the word"
    print("The size of the data \
    is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the \
    encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the \
    decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2
    a_great_sentence = "AAAAAABBBBBBBBCCCCCCCCCDDDDDAAAAA"
    print("The size of the \
    data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the \
    encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the \
    decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
