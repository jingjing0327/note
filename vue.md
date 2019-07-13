 <keep-alive exclude="home"></keep-alive>

# 发出去
this.$router.push({path:"/spu/createGoods",query:{id:row.id}})
# 接收
var id = this.$route.query.id;