Spring 注解
	@Repository
	@Component
	@RestController
	@Controller
	@ResponseBody
	@GetMapping
	@Autowired
	@Bean


Spring boot + Spring Security


vue 前后端分离，spring Security是怎么做的呢？

Api接口传递的参数验证：
推荐使用@Valid注解的方式，在方法参数多传递一个BindingResult error参数，所有的参数就是放到这个对象里面

@JsonView 可以指定那些值显示，那些值不显示。在显示相同字段时候，不同Controller的时候去选择；
使用接口来声明多个视图
在值对象的get方法上指定视图
在Controller方法上指定视图



@PostMapping
@GetMapping

MockMvc 在测试用例上非常方便的使用

## id 这样就可以作为变量来使用了
访问的换就可以 /user/1234
这里的1234位用户的id
@RequestMapping(value="/user/{id}",method=RequestMethod.GET)
public User getInfo(@PathVariable String id){
	
}




@Aspect
把这个类声明为一个切面，需要把该类放入到IOC容器中，在声明为一个切面

@Pointcut
定义一个方法，用于声明切入点表达式。一般地，该方法中不需要添入其他的代码。
	demo：
		@Pointcut("execution(public int com.xxx.*(...))")
		
		public void declareJointPointExpression(){

		}
		
		@Before("declareJointPointExpression")


@Component

@Before
声明改方法是一个前置通知，在目标方法开始之前执行
@AfterReturning
@AfterThrowing
@After
@Around

@Order
指定切面的优先级，值越小优先级越高

@Transactional
添加事务注解
最后你要在Application类中开启事务管理，开启事务管理很简单，只需要@EnableTransactionManagement注解就行



JWT
jpa

lombok ===>>>这他妈又是个啥？简化实体类的编写


Validator 验证框架

@NotNull
@Null
@Pattern
@Size(min=,max=)
@Emall
@Lenght(min=,max=)
@NotBlank
@NotEmpty
@Range(min=,max=)
@SafeHtml
@URL



HV000030: No validator coul 
int long 不能用@NotBlank 应该使用@NotNull

如果出现对象嵌套怎么办？
@Valid
private List<OrderInfo> orderInfoList;
直接@Valid来判断进行下一步类的判断

@Validated

public JsonResult createSKU(@Valid @RequestBody List<SKUInfo> skuInfos, BindingResult bindingResult)
@Valid 是不会验证List的

@RestController
@RequestMapping("/manage")
@Validated
public class SKUController {

需要在Controller上面加上个注解@Validated

@Validated是错误的解决方法，
正确方法是：

public class ValidList<E> {

    @Valid
    private List<E> list;

    public List<E> getList() {
        return list;
    }

    public void setList(List<E> list) {
        this.list = list;
    }
}

使用类去包裹一下，@Valid只能验证类

二级缓存