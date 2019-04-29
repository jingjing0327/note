
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