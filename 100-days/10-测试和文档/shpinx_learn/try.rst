部分
########

章节
*********

小章节
========

子章节
--------

子章节的子章节
^^^^^^^^^^^^^^^^^^

段落
""""""""""""

这是第一段

这是第二段这个还是第二段


*text*

**text**

`interpreted text`

``inline literal``

A :sub:`xxx`

A :sup:`xxx`

::

    some codes
    some codes

没有缩进，正常段落！

.. code-block:: python

    def some_function():
        interesting = False
        print 'This line is highlighted.'
        print 'This one is not...'
        print '...but this one is.'





.. sidebar:: this is a sidebar

    this is a sidebar, can insert code and image and so on.

冬日，在暖暖的午后，泡上一杯茶，随便拿起一本书，凑到阳光跟前，是何等的惬意与享受……

风虽然不大，但走在路上，鼻子冷的刺骨的疼；而阳光却那么地温热，温热地忍不住想和她亲吻。

我泡上一杯碧螺春，从书架上随便拿起一本书，走向靠窗的位置，凑到阳光面前，任由她吻着我的脸，就像吻着自己的情人，这感觉美好的让你忘却了所有的烦恼。

也许是身边暖气的缘故，空气的影子，映衬到桌子上、书纸上。影影绰绰如月下之花影，飘飘忽忽如山间之云



.. table:: Try table
    :name: table-table

    +------------+-----------+-----------+
    | column1    | h2        | h3        |
    +============+===========+===========+
    | body row   | c2        | c3        |
    +------------+-----------+-----------+
    | body 2     | ...       | ...       |
    +------------+-----------+-----------+


.. NOTE:: SOME NOTES
.. some comments
    rojweptjo
    jjogepw

jpogejwo


行内公式 :math:`\alpha > \beta` :

Display 公式:

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k



多行公式:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2


对齐多行公式:

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2


.. image:: insertfigure.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: 对于不能显示图片的时候, 显示这些文字
   :align: right


.. tip:: This is a tip

.. note:: This is a note

.. hint:: This is a hint

.. danger:: This is a danger

.. error:: This is an error

.. warning:: This is a warning

.. caution:: This is a caution

.. attention:: This is an attention

.. important:: This is an important

.. .. seealso:: This is seealso

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

This is a paragraph that contains `a link`_.

.. _a link: http://example.com/

你看到了吗? 第二个单词 word |word| !

.. |word| replace:: 替换成我了

.. :abbr:`LIFO (last-in, first-out)`

.. :command:`ls`

:math:`\alpha`

.. code:: python

  def my_function():
      "just a test"
      print 8/2

.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)




























































