def copy_dict(in_dict):
    # out_dict = dict()
    # for key, value in in_dict.items():
    #     out_dict[key] = value
    # return out_dict

    # return {key: val for key, val in in_dict.items()}
    return {key: in_dict[key] for key in in_dict}


if __name__ == '__main__':
    dict_list = [
        dict(s1='Hello ', s2='world'),
        dict(l1=[1, 2, 3], l2=[10, 12], l3=[4, 5, 6]),
        dict(f1=0.1, f2=0.2, i1=3, i2=123),
    ]

    for dict_in in dict_list:
        dict_out = copy_dict(dict_in)
        print(f"Test: {dict_in}")
        assert dict_in is not dict_out

    print("All test complete")
