yunSoDuuk = int(input("연소득 입력> "))
jeaJik = int(input("재직기간 입력> "))

if yunSoDuuk >= 40000000 and jeaJik >= 2:
    print("대출 자격 있음")
else:
    if yunSoDuuk < 40000000 and jeaJik >= 3:
        print("연봉 4000만원 이상 필요")
    else:
        if yunSoDuuk >= 40000000 and jeaJik < 2:
            print("재직기간 2년 이상 필요")
        else:
            print("연봉 4000만원 이상, 재직기간 2년 이상 필요")