class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # divide and conquer --> elimnate half sums at each iteration

        res = []

        sums.sort() 

        def divide_and_conquer(arr):
            # base case
            if len(arr) == 1:
                return []

            x = arr[1] - arr[0] # my candidate for original array
            # first max and second max cant be a candidate coz of -ve numbers present

            # use counter and split the array into two
            c = Counter(arr)
            without_x, with_x = [],[]
            for num in arr: # based on property of subset sums
                if c[num] > 0:
                    without_x.append(num)     # half group without adding x (Group A)
                    with_x.append(num + x)    # all elements in Group A + x
                    c[num] -= 1
                    c[num + x] -= 1

            # now we have successfully split group
            # we ignore the half and conquer the other

            # if 0 didnt appear in without_x, it means we wrongly picked the sign of x
            if 0 in without_x:
                res.append(x)
                divide_and_conquer(without_x)
            else:
                res.append(-x)
                divide_and_conquer(with_x)  # groups got flipped, coz of flipping sign

        divide_and_conquer(sums)

        return res




            

            

        return res
        