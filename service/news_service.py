from db.news_dao import NewsDao

class NewsService:
    __news_dao=NewsDao()

    # 查询待审批新闻列表
    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)
