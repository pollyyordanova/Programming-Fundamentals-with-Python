def redistribute_wealth(wealth_list, min_wealth):
    total_wealth = sum(wealth_list)
    required_wealth = len(wealth_list) * min_wealth

    if total_wealth < required_wealth:
        return "No equal distribution possible"

    for i in range(len(wealth_list)):
        if wealth_list[i] < min_wealth:
            needed = min_wealth - wealth_list[i]

            wealthiest = wealth_list.index(max(wealth_list))

            if wealth_list[wealthiest] - needed >= min_wealth:
                wealth_list[wealthiest] -= needed
                wealth_list[i] += needed
            else:
                wealth_list[i] += wealth_list[wealthiest] - min_wealth
                wealth_list[wealthiest] = min_wealth

    return wealth_list


if __name__ == "__main__":
    population = list(map(int, input().split(", ")))
    min_wealth = int(input())
    result = redistribute_wealth(population, min_wealth)
    print(result)




