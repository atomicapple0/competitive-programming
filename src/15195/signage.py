m = int(input().strip())
# m = 26

words = 'WELCOME TO CCC GOOD LUCK TODAY'.split(' ')

w = 0
while w < len(words):
    w_new = w
    line_length = len(words[w_new])
    w_new += 1
    while w_new < len(words):
        if line_length + len(words[w_new]) + 1 > m:
            break
        line_length += len(words[w_new]) + 1
        w_new += 1
    extra_room = m-line_length
    words_in_line = w_new - w
    additional_space = -1
    additional_space_for_first_couple = -1
    if words_in_line > 1:
        additional_space = extra_room // (words_in_line - 1) + 1
        additional_space_for_first_couple = extra_room % (words_in_line - 1)

    # print(f' ``` dbg: w:{w}, wn:{w_new}, er:{extra_room}, wil:{words_in_line}, as:{additional_space}, asffc:{additional_space_for_first_couple}')
    # print('/' * m)
    
    line = words[w]
    for i in range(words_in_line - 2):
        line += '.' * additional_space
        if i < additional_space_for_first_couple:
            line += '.'

        line += words[w + i + 1]
    if words_in_line > 1:
        left = m - len(line) - len(words[w_new-1])
        line += '.' * left
        line += words[w_new-1]
    else:
        line += '.' * (m - len(line))
    print(line)

    w = w_new
