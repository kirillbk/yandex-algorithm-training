<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Interactor</h1></div>
   <div class="legend"> Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи. <!--l. 50-->
      <p style="text-indent: 0em;">До заверщения очередной стадии проекта осталось написать модуль, определяющий <span style="font-style:
      italic;">итоговый вердикт </span>системы для интерактивной задачи. <span style="font-style: italic;">Итоговый вердикт </span>определяется
      из кода завершения задачи, вердикта интерактора и вердикта чекера по следующим правилам: </p><ul>
      <li>Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно. </li>
      <li>Код завершения задачи — это целое число от -128 до 127 включительно. </li>
      <li>Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и вердикту
      чекера в противном случае. </li>
      <li>Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера. </li>
      <li>Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и 4
      в противном случае. </li>
      <li>Если интерактор выдал вердикт 6, итоговый вердикт равен 0. </li>
      <li>Если интерактор выдал вердикт 7, итоговый вердикт равен 1. </li>
      <li>В остальных случаях итоговый вердикт равен вердикту интерактора.</li>
      </ul>
      <!--l. 76-->
      <p style="text-indent: 0em;">Ваша задача — реализовать этот модуль. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Входной файл состоит из трёх строк. В первой задано целое число <!--l. 79--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> (<!--l. 80--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"> <mo>−</mo> <mn>1</mn><mn>2</mn><mn>8</mn> <mo>≤</mo> <mi>r</mi> <mo>≤</mo> <mn>1</mn><mn>2</mn><mn>7</mn></math>)
      — код завершения задачи, во второй — целое число <!--l. 81--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>
      (<!--l. 81--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo>
      <mi>i</mi> <mo>≤</mo> <mn>7</mn></math>) — вердикт интерактора, в третьей — целое число <!--l. 82--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> (<!--l. 82--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo> <mi>c</mi> <mo>≤</mo> <mn>7</mn></math>)
      — вердикт чекера. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы. </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>0<br>0<br>0</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>-1<br>0<br>1</td>
            <td>3</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>42<br>1<br>6</td>
            <td>6</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 4</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>44<br>7<br>4</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 5</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>1<br>4<br>0</td>
            <td>3</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 6</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>-3<br>2<br>4
</pre></td>
            <td>2</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Кольцевая линия метро</h1></div>
   <div class="legend"><span style="">
         <p>Витя работает недалеко от одной из станций кольцевой линии Московского метро, а живет рядом с другой станцией той же линии.
            Требуется выяснить, мимо какого наименьшего количества промежуточных станций необходимо проехать Вите по кольцу, чтобы добраться
            с работы домой.
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Станции пронумерованы подряд натуральными числами 1, 2, 3, …, N (1-я станция – соседняя с N-й), N не превосходит 100.</p></span><p>Вводятся три числа: сначала N – общее количество станций кольцевой линии, а затем i и j – номера станции, на которой Витя
         садится, и станции, на которой он должен выйти. Числа i и j не совпадают. Все числа разделены пробелом.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Требуется выдать минимальное количество промежуточных станций (не считая станции посадки и высадки), которые необходимо проехать
            Вите.
         </p></span><p></p>
   </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>100 5 6</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>10 1 9</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Пояснения к примерам:</p></span><p>1) На кольцевой линии 100 станций; проехать с 5-й на 6-ю станцию Витя может напрямую, без промежуточных станций</p>
      <p>2) На кольцевой линии 10 станций; проехать с 1-й на 9-ю станцию Витя может через одну промежуточную, ее номер 10</p>
   </div>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Даты</h1>
   </div>
   <div class="legend"> Как известно, два наиболее распространённых формата записи даты — это европейский (сначала день, потом месяц, потом год)
      и американски (сначала месяц, потом день, потом год). Системный администратор поменял дату на одном из бэкапов и сейчас хочет
      вернуть дату обратно. Но он не проверил, в каком формате дата используется в системе. Может ли он обойтись без этой информации?
      <!--l. 51-->
      <p style="text-indent: 0em;">Иначе говоря, вам даётся запись некоторой корректной даты. Требуется выяснить, однозначно ли
      по этой записи определяется дата даже без дополнительной информации о формате. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Первая строка входных данных содержит три целых числа — <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,
      <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>
      и <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>
      (<!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>x</mi> <mo>≤</mo> <mn>3</mn><mn>1</mn></math>, <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <mi>y</mi> <mo>≤</mo> <mn>3</mn><mn>1</mn></math>, <!--l. 55--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>9</mn><mn>7</mn><mn>0</mn> <mo>≤</mo> <mi>z</mi> <mo>≤</mo> <mn>2</mn><mn>0</mn><mn>6</mn><mn>9</mn></math>.
      Гарантируется, что хотя бы в одном формате запись <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math><!--l.
      56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math><!--l. 56--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> задаёт корректную
      дату. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите 1, если дата определяется однозначно, и 0 в противном случае. </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>1 2 2003</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>2 29 2008</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В первом примере при одной системе записи дата равна 1 февраля, при другой - 2 января 2003 года, то есть однозначно назвать
      дату не получается. <!--l. 64-->
      <p style="text-indent: 0em;">Во втором примере корректный вариант даты может быть только в американском формате, где она задаёт
      29 февраля 2008 года. </p>
      
   </div>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Строительство школы</h1>
   </div>
   <div class="legend"><span style="">
         <p>В деревне Интернетовка все дома расположены вдоль одной улицы по одну сторону от нее. По другую сторону от этой улицы пока
            ничего нет, но скоро все будет – школы, магазины, кинотеатры и т.д.
         </p></span><p>Для начала в этой деревне решили построить школу. Место для строительства школы решили выбрать так, чтобы суммарное расстояние,
         которое проезжают ученики от своих домов до школы, было минимально.
      </p>
      <p>План деревни можно представить в виде прямой, в некоторых целочисленных точках которой находятся дома учеников. Школу также
         разрешается строить только в целочисленной точке этой прямой (в том числе разрешается строить школу в точке, где расположен
         один из домов – ведь школа будет расположена с другой стороны улицы).
      </p>
      <p>Напишите программу, которая по известным координатам домов учеников поможет определить координаты места строительства школы.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводится число N — количество учеников (0 &lt; N &lt; 100001). Далее идут в строго возрастающем порядке координаты домов
            учеников — целые числа, не превосходящие <span class="tex-math-text">2 &times; 10<sup>9</sup></span> по модулю.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно целое число — координату точки, в которой лучше всего построить школу. Если ответов несколько, выведите любой
            из них.
         </p></span><p></p>
   </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>4<br>1 2 3 4</td>
            <td>3</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>3<br>-1 0 1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Точка и треугольник</h1>
   </div>
   <div class="legend"><span style="">
         <p>На координатной плоскости расположены равнобедренный прямоугольный треугольник ABC с длиной катета d и точка X. Катеты треугольника
            лежат на осях координат, а вершины расположены в точках: A (0,0), B (d,0), C (0,d).
         </p></span><p>Напишите программу, которая определяет взаимное расположение точки X и треугольника. Если точка X расположена внутри или на
         сторонах треугольника, выведите 0. Если же точка находится вне треугольника, выведите номер ближайшей к ней вершины.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводится натуральное число d (не превосходящее 1000), а затем координаты точки X – два целых числа из диапазона от
            ­–1000 до 1000.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Если точка лежит внутри, на стороне треугольника или совпадает с одной из вершин, то выведите число 0. Если точка лежит вне
            треугольника, то выведите номер вершины треугольника, к которой она расположена ближе всего (1 – к вершине A, 2 – к B, 3 –
            к C). Если точка расположена на одинаковом расстоянии от двух вершин, выведите ту вершину, номер которой меньше.
         </p></span><p></p>
   </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>5<br>1 1</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>3<br>-1 -1</td>
            <td>1</td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>4<br>4 4</td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 4</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>4<br>2 2</td>
            <td>0</td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Комментарии к примерам тестов</p></span><p>1. Точка лежит внутри треугольника.</p>
      <p>2. Точка лежит вне треугольника и ближе всего к ней вершина A</p>
      <p>3. Точка лежит на равном расстоянии от вершин B и C,в этом случае нужно вывести ту вершину, у которой номер меньше, т.е. выведено
         должно быть число 2
      </p>
      <p>4. Точка лежит на стороне треугольника.</p>
   </div>
</div>