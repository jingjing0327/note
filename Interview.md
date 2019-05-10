https://github.com/AweiLoveAndroid/CommonDevKnowledge/blob/master/interview/contents/java%E9%9D%A2%E8%AF%95%E9%A2%98.md

# java中==和equals和hashCode的区别

	java中的数据类型分为两种：
	基本数据类型
		byte,short,chat,int,long,float,doubel,boolean
		基本数据类型比较的话，用==来比较
	引用数据类型（类，接口，数组）
		当他们用==的时候，对比的是内存存放地址，所有除非是new出来的对象，不然就是false
		对象是放在堆中的，栈中存放的是对象引用地址。因此==是对栈中的内存地址进行比较。如果要比较堆中的对象，需要重新equals方法了。
		equal是object的方法
	hashCode()方法返回的是一个int数值，其中他的目的是生成一个hash码。hash码的主要途径就是进行三列的时候最为key输入，对象的每个hash码尽可能的不同，这要才能保证三列的存取性能。Object累提供的默认实现已经保证每个对象的hash码不同，在内存地址的基础上经过一个算法返回一个hash码。

	在每个覆盖了equals方法的类中，也必须要覆盖hashCode方法，如果不这样做的话，就会违反Object.hashCode的通用约定，从而导致该类无法结合所有基于散列的集合一起正常工作，这样的集合包括HashMap、HashSet和HashTable

	如果不处理HashCode的话，数据会容易重复。

# int和Interger的区别
	一个是基本数据类型，一个是引用数据类型

# 多态
	指允许不同类的对象对同一个消息做出响应。即同一消息可以根据发送对象的不同而采用多种不同的行为方式。（发送消息就是函数调用）
	作用就是：消除类型之间的耦合关系

# String,StringBuffer与StringBuilder的区别
	String的值是不可变的，所以就导致了每次对String的操作都会产生一个新的String对象。这样的效率非常的低，而且有会大量的浪费内存空间。

	所有就有了StringBuffer和StringBuilder的出现，这两个类的对象可以被多次修改，而不产生新的内存空间。

	StringBuilder 线程不安全，执行速度快
	StirngBuffer 线程安全，执行速度慢
	他们两个都继承AbstractStringBuilder

# 什么是内部类？内部类的作用
	将一个类定义在另一个类里面或者一个方法里面，这样的类称为内部类。
	方便于写线程代码
	在OKHttp里面实例化的时候，也会有内部类的实现。
# 抽象类和接口区别
	abstract class 里面有抽象方法，也可以定义实现好的方法。
	如果你拥有一些方法并且想让他们中默认实现，那么就是用抽象方法。如果你想多继承就使用接口。
# 抽象类的意义
	抽象类的意义：对代码的维护和重用。
	抽象类不能别实例化，所以经常抽象类的子类来实现抽象类的方法。
	是java面相对象的一个重要体现。
# 抽象类是否可以没有方法和属性?
	可以。抽象类可以没有方法和抽象方法，但是有抽象方法的class一定是抽象类。
# 泛型中extends和super的区别
	List<? super T>、Set<? extends T>的声明，是什么意思呢？<? super T>表示包括T在内的任何T的父类，<? extends T>表示包括T在内的任何T的子类
# 进程和线程的区别
	进程：是指执行的程序在执行过程中分配和管理资源的基本单位，是个动态概念。
	线程：是进程的执行单元，。
	一个程序至少有一个进程，一个进程至少有一个线程。
# 序列化的方式
	什么是序列化？对象转成字节流
	什么是反序列化？字节流转对象
	为啥要序列化？
	要永久的保存对象，保存对象的字节流到本地文件中。
	通过序列化对象在网络中传输
	通过序列化在进程中传递
	
	Serializable 接口
	parcelable 接口
# 静态属性和静态方法是否可以被继承？是否可以被重写？以及原因？
	不能。
	静态属性和静态框架只初始化一次。
# 静态内部类的设计意图
		
# 成员内部类、静态内部类、局部内部类和匿名内部类的理解,以及项目中的应用
	成员内部类：是最普通的内部类，它定义为位于另一个类的内部，成员内部类是可以无条件的访问外部类的所有成员属性和成员方法的，包括private私有成员还静态成员。
	然而外部类想访问内部类，就需要new出一个新的内部类的引用来访问了。

	静态内部类：定义在成员变量的位置上，并且用static来去修饰他。

	局部内部类：就像方法里面的局部变量一样，但是不能有public，private，protected，static的修饰符。

	匿名内部类：一般是在回调的时候使用，比如说点击事件啊 ，线程啦。没有名字的类。


# 谈谈对kotlin的理解

# 闭包和局部内部类的区别
	闭包：内部类使用了外部类的局部变量，实际上形成了闭包，也就是获取了所在方法内的变量，这个被捕获的变量不能随着方法的执行完毕而消失，因为内部类的实例可能还会用到这个变量，所有需要final关键字来让这个变量不消失。

# string 转换成 integer的方式及原理
	首先是要判断是否为null，第一个判断是符号，然后遍历，然后返回结果，在里面会抛出一个异常，NumberFormatException

======================================
# 哪些情况下的对象会被垃圾回收机制处理掉？
	应用计数法，就是在对象的都上面维护一个计数器Counter，当有一个引用指向对象的时候couter就是加一，当不在引用此对象时就让counter减一。当couter为0的时候，就是把扎个对象回收。这种方法存在致命的问题，就是。外部对对象A有一个引用，对象A持有对象B，而对象B也持有一个对象C，对象C又持有对象A。如果对于对象A的引用r失效，按照引用计数方法，GC永远无法回收上面的三个对象。

	可达行分析算法，java就是使用此方法作为判断对象是否可以被回收的。虚拟机会将对象定义为GC Roots，从GC Roots出发一直引用链向下寻找，如果摸个对象不能通过GC Roots寻找到，那么虚拟机就认为对象可以被回收。
	那么什么样的对象可以被看做是GC Roots呢？
		虚拟机栈中的应用对象
		方法区中的类静态属性引用的对象
		方法区中常量引用的对象
		本地方法栈中JNI（Native方法）的引用对象
# 讲一下常见编码方式？
	UTF-8,iso8859-1,gbk,
# utf-8编码中的中文占几个字节；int型几个字节？
	中文是4个字节
	int是1个字节
# 静态代理和动态代理的区别,什么场景使用?
	代理是一种软件设计模式，目的就是希望能做到代码的重用。这种的设计模式是说不通过代码来访问对象的方式，而是通过代理的方式来访问对象。

	比如说我在接手前人的代码时候，里面的代码逻辑可能让人摸不到头脑，这时候就很难去下手去修改，这个时候我们就通过代理的方式去进行类的增强。

	那是一种解耦合的一种表现，不去直接访问对象。

	spring的AOP机制思想就是采用了动态代理的机制来是实现的面相切面编程。

	静态代理：
		创建一个接口，java api代理机制要求被代理的类必须实现某个接口，对于静态代理方式代理类也要是实现和被代理相同的接口；

	动态代理：
		动态代理则不需要实现被代理类所实现的接口，而是通过反射实现的接口。
		InvocationHanlder 实现这个接口
		invoke 方法
# Java的异常体系
	Throwable 是所有异常类的父类。
	Error、Exception

# 谈谈你对解析与分派的认识。

# 修改对象A的equals方法的签名，那么使用HashMap存放这个对象实例的时候，会调用哪个equals方法？
	当然是对象的equals了啊

# Java中实现多态的机制是什么？
	重写overRead 是父类与子类的之间多态性的一种表现
	重载overLoad 是一个类中多态性的一种表现

# 如何将一个Java对象序列化到文件里？
	序列化：
		Serializable 
		FileOutputStream
		ObjectOutputStream.writeObject(student)
	反序列化：
		Serializable
		FileInputStream
		Strdent=ObjectInputStream.readObject();

# 说说你对Java反射的理解
	反射是能够分析类能力的程序

	可以在程序运行过程中分析类的能力
	在运行中查看对象，例如变下一个toString方法供所有类去使用
	实现数组的操作代码
	利用Method对象

# 说说你对Java注解的理解	

# 说说你对依赖注入的理解
	spring的依赖注入，可以理解为想用什么就是直接拿什么，那不是像之前一样去new什么，用xml或者注解，告诉我你要什么，我就给你什么。

# 说一下泛型原理，并举例说明
	泛型的本质是参数化类型，也就是说所操作的数据类型被指定为一个参数。这种参数类型可以用在类、接口和方法的创建中，分别称为泛型类、泛型接口、泛型方法。
	泛型可以消除代码中的强制类型装换，同时获得一个附加的类型检查层，该检查层可以防止有人将错误类型的键或值保存在集合中。这就是泛型所做的工作。
	
	类型擦除

	好处：
		类型安全。
		消除强制类型装换。
		潜在的性能收益。

# Java中String的了解
	String是final类型，也就是意味着String类是不是能被继承的，并且他的成员方法都默认是final方法。
	String类其实是通过char数组来保存字符串的。
	String对象一旦被创建就是固定不变的，对String对象任何操作和改变都不影响原来的对象，相关的任何chang操作都会生成新的对象。

	jvm常量池
	静态常量池和运行时常量池。
	静态常量池，就是*.class文件中的常量池。
	运行时常量池，则是jvm虚拟机在完成类装载操作后，讲class文件中的常量池载入到内存中，并保持在方法区中。

	String a = "chenssy";
	String b = "chenssy";
	a、b和字面上的chenssy都是指向JVM字符串常量池中的"chenssy"对象，他们指向同一个对象。

	String aa="abc" 和 Sting aa=new String("abc")这两个有什么区别呢？
	=的话是直接在jvm常量池中寻找或者创建
	new是在现在jvm常量池中寻找或者创建，之后在堆中创建一个新的对象，指向内存地址

# String为什么要设计成不可变的?
	不可变支持线程安全
	不可变支持字符串常量池，提升性能

# 常用数据结构简介

# 并发集合了解哪些？

# 列举java的集合以及集合之间的继承关系

# 集合排序，比较器

# 集合类以及集合框架
	Collection 包含List和Set
	List包含：LinkedList、ArrayList、Vector
	Set包含：HashSet、TreeSet、SortedSet

	Map包含：HashMap、WeakHaskMap、TreeMap、SortedMap
	HashMap有entrySet Set<Map.Entry<K,V>> Set 集合
	所以它可以遍历



# List,Set,Map的区别
	List
		ArrayList
		LinkedList
		Vector
	Set
		HashSet
	Map
		HashMap
		ConcurrentHashMap
		LinkedHashMap
		ArrayMap
		TreeMap
		HashTable

	==============================
	==============================
	==============================
	==============================
	ArrayList是一个数组队列，相当于动态数组，他的容量能动态增长。
	线程不安全的。
	初始大小为10
	int newCapacity = (oldCapacity * 3)/2 + 1;
	新的容量是旧容量 * 3 / 2
	3种遍历方式：
		1、因为ArrayList有RandomAccess接口的实现，所有他支持随机访问。
		2、迭代器
		3、for循环

	LinkedList是双向链表。实现了List接口，能对它进行排序操作。
	双向链表：就是除去头和尾部分，中间的值是保存了上一个和下一个的内存地址。

	Vector 是队列，是安全的，所有的方法都加了锁。
	实际上是通过数组去保存数据的，默认的容量是10
	当Vector容量不足一容纳全部元素的时候，Vector的容量会增加。若容量增加系数>0，则将容量的值增加“容量增加系数”；否则就是将大小增加一倍。
	
	HashMap是线程不安全的，于是就是出现了HashTable，HashTable的实现方法和HashMap的实现方法是一样的，只是hashTable是线程安全的，并且不允许为null，key和value都不允许为null。但是HashTable的安全策略比较简单粗暴，put/get的所有操作都加上了锁，syschronized。这样的话，性能就大大打了折扣。
	于是就出现了ConcurrentHashMap,他的设计是非常精妙的分段锁策略。他的主干就是一段一段的数组，segment数组。每个数组维护一个锁，默认ConcurrentLevel为16，也就是说可以有16线程并发嘛。所以，对于同一个segment才去考虑线程同步。
	一个segment维护一个HashEntry数组。
	hashEntry是最小处理单元。
	Segment数组的大小通过散列算法实现。

	哈希函数：哈希表的主干是数组。
	为啥哈希会比较快：通过哈希函数计算出实际的存储地址，然后从数组中对应的地址取出值即可！
	哈希冲突：
	这是必然的，两个不同的原始，通过哈希算法得出的实际存储地址是相同的。
	HashMap的解决方法：数组+链表的方式。
	get的方法：key-haskcode-hash-indexFor-最终索引地址，table[i]，得到位置之后，在查看是否有链表，遍历链表，通过key的query方法进行查找对应的记录。

	jdk1.8后，java对HashMap做了改进，在链表长度大于8的时候，将后面的数据存在红黑树中，以加快检索的速度。

	
	Set里存放的对象是无序，不能重复的，集合中的对象不安特定的方式排序，只是将对象加入到集合中。
	HashSet的构造方法第一句就是map=new HashMap<E,Object>，是用了HashMap的key来实现各种特性，不允许重复，允许null值，非线程安全的。

	LinkedHashMap有一个数组保存了插入的顺序。
	
	ArrayMap内部有两个比较重要的数组，一个是mHashes，另一个是mArray。
	mHashes是用来存放key的hashcode值，是从小到大的排序方式。
	mArray是用来存放key与value的值，是mHashes大小的2倍。


	SparseArray比HashMap更省内存，在某些条件下性能更好，主要是避免了对key的自动装箱。是通过两个数组来进行数据存储的，一个存储是key，另外一个存储是value。SparseArray只能存储key为int类型的数据，同时在存储和读取数据时候，使用的是二分才查找发。key，value是按照从小到大的顺序排列好的。





# 多线程
	继承Thread
	实现Runnable
	实现Callable






