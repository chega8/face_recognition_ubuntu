# Code Style

1.  **Код	должен	соответствовать общепринятому стандарту	PEP	8**
При	использовании	PyCharm	для	написания	кода IDE	подсвечивает	места,	в	которых	код	не	
соответствует	принятому	стандарту.
Подробнее:	https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
2. **Не	допускать	использования «магических	констант» в	коде**
Исключение:	запись	формул	(в	этом	случае	следует	в	комментариях записать	
аналитический	вид	формулы	или	указать	ссылку).
3. **При	определении	методов следует	указывать	типы	аргументов	и возвращаемого	значения**
Подробнее:	https://docs.python.org/3/library/typing.html
4. **Не	допускать	использования приватных	методов в	классах**
Пояснение:	как	показывает	практика,	разработчики	оборачивают	кучу	нечитаемого	кода	
в	приватные	методы.	Пишите	код	так,	как	будто	его	будет	читать	маньяк,	который	
знает,	где	вы	живете.
5. **Все	классы должны наследоваться	либо	от	«object»,	либо	от	других	классов**
6. **Для	всех	классов	следует	определять	поле	«__slots__» с	целью экономии памяти**
Подробнее:	http://book.pythontips.com/en/latest/__slots__magic.html
7. **В	качестве	отступов следует	использовать	4	пробела**
PyCharm	автоматически	заменяет	табуляцию	на	пробелы.
8. **Для	форматирования	строк	следует	использовать	оператор	%**
Исключение:	конкатенация	строковых	переменных.
Пример:	
``'name: %s; score: %d' % (name, n)``
9. **Использовать TODO-комментарии для обозначения временного	кода,	
краткосрочной	заплатки,	либо	хорошего,	но	не	идеального	решения**
Пример:
``#TODO(kl@gmail.com): Use a "*" here for string repetition.``
``#TODO(Zeke) Change this to use relations.``
10. **Импорты	должны	быть	сгруппированы	в	следующем	порядке:**
1) Импорты	из	стандартной	библиотеки
2) Сторонние	импорты
3) Импорты	из	собственных	библиотек	(например,	biblioteka.core)




# Docstyle

**Использование	инлайновых	комментариев**
Комментарии,	начинающиеся	с	символа	«#»,	следует	использовать	только	при	описании	хитрых	мест в	коде	(например,	алгоритм	или	хитрая	оптимизация).	Такие	комментарии	не	должны	описывать	то,	что	делает	код	(например,	«инкрементирование	переменной	i»).	Предположите,	что	человек,	читающий	данный	код,	знает	Python	(а	не	то,	что	вы	пытаетесь делать)	лучше,	чем	вы.В	случае,	когда	комментарий	располагается	в	конце	строки,	содержащей	код,	следует	использовать	как	минимум	2	пробела	для	отступа от	кода	(для	улучшения	читаемости	кода).

**Документирование	функций	и	методов**
Функция	должна	иметь	строку	документации	во	всех	случаях,	кроме:
- Не	видима	снаружи	модуля
- Очень	короткая
- Очевидная	(легко	читаемая)
Строка	документирования	должна	давать	достаточно	информации,	чтобы	оформить	вызов	функции	
без	чтения	ее	исходного	кода.	Строка	документирования	должна	описывать	синтаксис	вызова	
функции	и	ее	семантику,	но	не	должна	описывать	ее	реализацию.	Для	хитрого	кода	комментарии	
внутри	исходного	кода	более	предпочтительны,	чем	строки	документации.
*Пример:*
```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
		 """Fetches rows from a Bigtable.
		
			Retrieves rows pertaining to the given keys from the Table instance
represented by big_table. Silly things may happen if other_silly_variable is
not None.
            Args:
			    big_table: An open Bigtable Table instance.
				keys: A sequence of strings representing the key of each table row to
fetch.
				other_silly_variable: Another optional variable, that has a much longer
name than the other args, and which does nothing.

		Returns:
			A dict mapping keys to the corresponding table row data fetched. Each
row is represented as a tuple of strings. For example:

		 {'Serak': ('Rigel VII', 'Preparer'),
		 'Zim': ('Irk', 'Invader'),
		 'Lrrr': ('Omicron Persei 8', 'Emperor')}

		 If a key from the keys argument is missing from the dictionary, then
that row was not found in the table.

		 Raises:
			 IOError: An error occurred accessing the bigtable.Table object.
 		"""
	pass
```

**Документирование	классов**
Классы	должны	иметь	строку	документации	ниже	своего	объявления.	Если	Ваш	класс	имеет	публичные	атрибуты,	они	должны	быть	документированы тут	же	в	разделе	Attributes	и	следовать	тому	же	стилю	форматирования,	что	и	раздел	Args.

*Пример:*

```python
class SampleClass(object):
	"""Summary of class here.

	 Longer class information....
	 Longer class information....

	Attributes:
 		likes_spam: A boolean indicating if we like SPAM or not.
		 eggs: An integer count of the eggs we have laid.
	 """

	def __init__(self, likes_spam=False):
		 """Inits SampleClass with blah."""
		 self.likes_spam = likes_spam
		 self.eggs = 0

	def public_method(self):
		 """Performs operation blah."""
```



