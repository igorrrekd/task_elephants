import sys

# method 1


def method_1(initial_sequence, final_sequence, load):
    sum1 = 0
    sequence = initial_sequence[:]
    Inf = 7000
    weight = load[:]

    while sequence != final_sequence:
        temporary_elephant = min(weight)
        nr_elephant = weight.index(temporary_elephant) + 1
        temporary_index = sequence.index(nr_elephant)

        nr_elephant_min = final_sequence[temporary_index]
        temporary_index_min = sequence.index(final_sequence[temporary_index])

        if sequence.index(nr_elephant) != final_sequence.index(nr_elephant):
            sequence[temporary_index] = nr_elephant_min
            sequence[temporary_index_min] = nr_elephant

            sum1 += temporary_elephant + weight[nr_elephant_min - 1]

        weight[nr_elephant_min - 1] = Inf

    return sum1

# method 2


def method_2(initial_sequence, final_sequence, load):
    sum2 = 0
    sequence = initial_sequence[:]
    Inf = 7000
    weight = load[:]

    while sequence != final_sequence:
        temporary_elephant = min(weight)
        nr_elephant = weight.index(temporary_elephant) + 1
        temporary_index = sequence.index(nr_elephant)

        nr_elephant_min = final_sequence[temporary_index]
        temporary_index_min = sequence.index(final_sequence[temporary_index])

        if sequence.index(nr_elephant) != final_sequence.index(nr_elephant):
            sequence[temporary_index] = nr_elephant_min
            sequence[temporary_index_min] = nr_elephant

            sum2 += temporary_elephant + weight[nr_elephant_min]

            if weight[nr_elephant_min - 1] != min(weight):
                weight[nr_elephant - 1] = Inf

        else:
            temporary_elephant_2 = sorted(weight)[1]
            nr_elephant_2 = weight.index(temporary_elephant_2) + 1
            temporary_index_2 = sequence.index(nr_elephant_2)

            temporary_elephant_min = min(weight)
            nr_elephant_min = weight.index(temporary_elephant_min) + 1
            temporary_index_min = sequence.index(nr_elephant_min)

            sequence[temporary_index_2] = nr_elephant_min
            sequence[temporary_index_min] = nr_elephant_2

            sum2 += temporary_elephant_2 + temporary_elephant_min

    return sum2


if __name__ == "__main__":

    with open(sys.argv[1]) as plik:
        linie = plik.readlines()

        load = list(map(int, linie[1].split()))
        initial_sequence = list(map(int, linie[2].split()))
        final_sequence = list(map(int, linie[3].split()))

    sum1 = method_1(initial_sequence, final_sequence, load)
    sum2 = method_2(initial_sequence, final_sequence, load)

    if sum1 > sum2:
        print(sum2)
    else:
        print(sum1)