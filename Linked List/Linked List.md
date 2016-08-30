### Linked List

#### 1. Introduction

*Linked List*, 链表。

首先，链表是数据结构(Data Structure)中比较基础的一种数据结构，是线性表的一种，抽象的一组包含多个元素的序列。链表中的多个元素是通过链接联系起来组成的一个表，每个链接连接着上一个元素和下一个元素，还包含一个元素，即存储的数据。

我们在此介绍简单单向链表，将链表进行可视化之后我们可以认为链表是具有以下结构的一个表，链表由一个个的节点(Node)前后连接起来组成的，每一个节点指向下一个节点，像链条一样。

​                              ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list.jpg)

通过上面的链表图片我们可以得到链表以及节点的结构：

* 在单向链表中包含一个头节点(**Header**)，头节点是不存储数据的，头节点作为指示链表开始的地方，并指向下一个节点数据区域；
* 每个节点(Node)包含两部分，数据区域(Data Field)和链接区域(Link Field)，数据区域存储每个节点的数据；
* 链接区域负责将此节点与下一个节点相连（指向下一个节点），进而组成整个链表；
* 链表中最后一个节点的链接区域指向Null，表示这一链表的结束。

#### 2. Basic Operations

链表属于线性表(顺序表)的一种，其涉及到的常见操作有：

- Insertion (插入)：向链表中添加元素，包括向链表的开头，结尾和中间某处处添加元素；
- Deletion (删除)：删除列表中的元素，开头、结尾和中间某个固定的元素；
- Display (显示)：显示整个链表；
- Search (检索)：在链表中检索某个元素；
- Clear (清空)：清空整个链表；

##### 2.1 Insert operation

在原来的链表中插入新的节点。

1. 首先，需要构建一个与原始链表中节点相同的插入节点，如下图；

   ​             ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_insertion_0.jpg)

2. 假设新的节点将要插入到上面两个节点的中间位置（左边为A节点，右边为C节点，下面的为C节点），那么我们需要让C节点的链接区域（Next）指向C节点的数据区域（Data Items），如下图所示；

   ```
   NewNode.Next -> RightNode 
   ```

   ​

   ​             ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_insertion_1.jpg)

3. 然后，再将A节点的链接区域指向C节点，如下图所示

   ```
   LeftNode.Next -> NewNode
   ```

   ​             ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_insertion_2.jpg)

   到此，新的节点已经完全插入到了原来的链表当中了，如下图所示。

   ​                 ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_insertion_3.jpg)

#####  2.2 Deletion

在链表中删除链表中的某个元素，也需要多个步骤。在此举例删除链表中的某个节点（非首尾节点，省略检索节点位置的过程），如下所示。

1. 首先，利用检索算法定位需要删除的节点的位置（略）；

   ​                  ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_deletion_0.jpg)

   如上图所示，假设中间的节点为要删除的目的节点，已定位；

2. 然后，将目的节点左边的节点的链接区域指向目的节点右边节点，如下图所示；

   ```
   LeftNode.Next -> TargetNode.Next
   ```

   ​                  ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_deletion_1.jpg)

3. 最后，删除目的节点的链接区域指向右边节点的链接，

   ```
   Target.Next -> Null
   ```

   ​                   ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_deletion_2.jpg)

   完成节点的删除之后的链表，如下图，

   ​                                       ![](https://lynnlaulsl.files.wordpress.com/2016/08/linked_list_deletion_3.jpg)



通过上面两个链表的基本操作，我们可以看到链表的增、删、改、查等都是需要多步操作，除此之外还有链表的反向等其他操作，在此不一一介绍。