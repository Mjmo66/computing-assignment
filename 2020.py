def get_new():
    new_name = input('what is your first name')
    new_secname = input('what is your second name')
    new_category = input('what is catergory are u in')
    new_password = input('enter your password')

    return new_name, new_secname, new_category,new_password




def r_data(new_name, new_secname, new_category,new_password):

    with open ("assignments/2020.cw/members.txt") as file:
        lines = file.readlines()
        linecount = len(lines)


        f_name  = [' ']* 50
        s_name  = [''] * 50
        category = [''] * 50
        password = [''] * 50
        tempstring = ['']* 4
     #   temparray = [None, None,None,None]
    
    with open ("assignments/2020.cw/members.txt") as file:
        for i in range(linecount):
            tempstring  = file.readline().strip()
            temparray   = tempstring.split(",")
            f_name[i]   = temparray[0]
            s_name[i]   = temparray[1]
            category[i] = temparray[2]
            password[i] = temparray[3]

        f_name[linecount] = new_name
        s_name[linecount] = new_secname
        category[linecount] = new_category
        password[linecount] = new_password
    
        print(f_name)

    return category


def cal_cat(category):
    # add code here
     print('csat')




def main():
	new_name, new_secname, new_category,new_password= get_new()
	category = r_data(new_name,new_secname, new_category,new_password)
    
	

main()
