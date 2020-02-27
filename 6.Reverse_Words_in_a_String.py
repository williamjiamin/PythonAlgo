def reverse_words_in_a_string_V4_without_built_in(s):
    length = len(s)
    spaces = [' ']
    words_list = []

    i = 0

    while i < length:
        if s[i] not in spaces:
            start_word = i

            while i < length and s[i] not in spaces:
                i += 1

            words_list.append(s[start_word:i])

        i += 1
    return "".join(reversed(s))


print(reverse_words_in_a_string_V4_without_built_in("My name is William"))
