from django.utils.safestring import mark_safe


class PageInfo(object):
    def __init__(self, current, totalItem, peritems=5):
        self.__current = current
        self.__peritems = peritems
        self.__totalItem = totalItem


    def From(self):
        return (self.__current - 1) * self.__peritems

    def To(self):
        return self.__current * self.__peritems

    def TotalPage(self):  # 总页数
        result = divmod(self.__totalItem, self.__peritems)
        if result[1] == 0:
            return result[0]
        else:
            return result[0] + 1


def Custompager(baseurl, currentPage, totalpage):  # 基础页，当前页，总页数
        perPager = 11
        # 总页数<11
        # 0 -- totalpage
        # 总页数>11
        # 当前页大于5 currentPage-5 -- currentPage+5
        # currentPage+5是否超过总页数,超过总页数，end就是总页数
        # 当前页小于5 0 -- 11
        begin = 0
        end = 0
        if totalpage <= 11:
            begin = 0
            end = totalpage
        else:
            if currentPage > 5:
                begin = currentPage - 5
                end = currentPage + 5
                if end > totalpage:
                    end = totalpage
            else:
                begin = 0
                end = 11
        pager_list = []
        if currentPage <= 1:
            first = "<a href=''><span class='upten'></span></a>"
        else:
            first = "<a href='%s%d'><span class='upten'></span></a>" % (baseurl, 1)
        pager_list.append(first)

        if currentPage <= 1:
            prev = "<a href=''><span class='up'></span></a>"
        else:
            prev = "<a href='%s%d'><span class='up'></span></a>" % (baseurl, currentPage - 1)
        pager_list.append(prev)

        sd = "<span class='split'></span>"
        pager_list.append(sd)

        yszt = "<span class='page_info_one'>第 %d/%d 页</span>"%(currentPage,totalpage)
        pager_list.append(yszt)

        pager_list.append(sd)

        if currentPage >= totalpage:
            next = "<a href='#'><span class='dowm'></span></a>"
        else:
            next = "<a href='%s%d'><span class='dowm'></span></a>" % (baseurl, currentPage + 1)
        pager_list.append(next)

        if currentPage >= totalpage:
            last = "<a href=''><span class='downten'></span></a>"
        else:
            last = "<a href='%s%d'><span class='downten'></span></a>" % (baseurl, totalpage)
        pager_list.append(last)

        ysjl ="<span class ='page_info_two' > 页记录数 %d 页 </span>"%(currentPage)
        pager_list.append(ysjl)

        result = ''.join(pager_list)
        return mark_safe(result)  # 把字符串转成html语言