<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Быстрый поиск в массиве</h1>
   </div>
  <div class="legend"> Дан массив из N целых чисел. Все числа от −10<sup>9</sup> до 10<sup>9</sup>. Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R".   
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Число N (1 ≤ N ≤ 10<sup>5</sup></math>). Далее N целых чисел.
    Затем число запросов K (1 ≤ K ≤ 10<sup>5</sup>).
    <p>Далее K пар чисел L, R (-10<sup>9</sup>  L ≤ R ≤ 10<sup>9</sup>) — собственно запросы. </p>
      <p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите <!--l. 59--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>
      чисел — ответы на запросы. 
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>
              5<br>10 1 10 3 4<br>4<br>
              1 10<br>
              2 9<br>
              3 4<br>
              2 2<br>
           </td>
            <td>5 2 2 0</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Номер левого и правого вхождения</h1>
   </div>
   <div class="legend"><span style="">
         <p>Требуется определить в заданном массиве номер самого левого и самого правого элемента, равного искомому числу. </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится одно натуральное число <span class="tex-math-text">N</span>, не превосходящее <span class="tex-math-text">10<sup>5</sup></span>: количество чисел в массиве. Во второй строке вводятся <span class="tex-math-text">N</span> натуральных чисел, не превосходящих <span class="tex-math-text">10<sup>9</sup></span>, каждое следующее не меньше предыдущего. В третьей строке вводится количество искомых чисел <span class="tex-math-text">M</span> &ndash; натуральное число, не превосходящее <span class="tex-math-text">10<sup>6</sup></span>. В четвертой строке вводится <span class="tex-math-text">M</span> натуральных чисел, не превосходящих <span class="tex-math-text">10<sup>9</sup></span>.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса выведите в отдельной строке через пробел два числа: номер элемента самого левого и самого правого элементов
            массива, равных числу-запросу. Элементы массива нумеруются с единицы.Если в массиве нет такого числа, выведите в соответствующей
            строке два нуля, разделенных пробелом.
         </p></span></div>
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
            <td>4<br>1 2 2 3<br>4<br>4 3 2 1</td>
            <td>0 0<br>4 4<br>2 3<br>1 1<br></td>
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
            <td>10<br>1 2 3 4 5 6 7 7 8 9<br>10<br>7 3 3 1 3 7 9 7 7 10<br></td>
            <td>7 8<br>3 3<br>3 3<br>1 1<br>3 3<br>7 8<br>10 10<br>7 8<br>7 8<br>0 0</td>
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
            <td>10<br>1 3 3 3 3 6 8 8 9 10<br>10<br>2 9 6 4 2 9 3 7 9 7<br></td>
            <td>0 0<br>9 9<br>6 6<br>0 0<br>0 0<br>9 9<br>2 5<br>0 0<br>9 9<br>0 0</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Корень кубического уравнения</h1>
   </div>
   <div class="legend"><span style="">
         <p>Дано кубическое уравнение <span class="tex-math-text">ax<sup>3</sup>+bx<sup>2</sup>+cx+d=0</span> (<span class="tex-math-text">a&ne;0</span>). Известно, что у этого уравнения есть ровно один корень. Требуется его найти.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входном файле через пробел записаны четыре целых числа: -1000 ≤ a, b, c ,d ≤ 1000.
         </p></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите единственный корень уравнения с точностью не менее 5 знаков после десятичной точки.</p></span></div>
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
            <td>1 -3 3 -1</td>
            <td>1.0000036491</td>
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
            <td>-1 -6 -12 -7</td>
            <td>-1.0000000111</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Вырубка леса</h1>
   </div>
   <div class="legend"><span style="">
         <p>Фермер Николай нанял двух лесорубов: Дмитрия и Федора, чтобы вырубить лес, на месте которого должно быть кукурузное поле.
            В лесу растут X деревьев. 
         </p></span><p>Дмитрий срубает по A деревьев в день, но каждый K-й день он отдыхает и не срубает ни одного дерева. Таким образом, Дмитрий
         отдыхает в K-й, 2K-й, 3K-й день, и т.д. 
      </p>
      <p>Федор срубает по B деревьев в день, но каждый M-й день он отдыхает и не срубает ни одного дерева. Таким образом, Федор отдыхает
         в M-й, 2M-й, 3M-й день, и т.д. 
      </p>
      <p>Лесорубы работают параллельно и, таким образом, в дни, когда никто из них не отдыхает, они срубают A + B деревьев, в дни,
         когда отдыхает только Федор — A деревьев, а в дни, когда отдыхает только Дмитрий — B деревьев. В дни, когда оба лесоруба отдыхают,
         ни одно дерево не срубается. 
      </p>
      <p>Фермер Николай хочет понять, за сколько дней лесорубы срубят все деревья, и он сможет засеять кукурузное поле. </p>
      <p>Требуется написать программу, которая по заданным целым числам A, K, B, M и X определяет, за сколько дней все деревья в лесу
         будут вырублены. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Входной файл содержит пять целых чисел, разделенных пробелами: A, K, B, M и X (1 ≤ A, B ≤ <span class="tex-math-text">10<sup>9</sup></span> , 2 ≤ K, M ≤ <span class="tex-math-text">10<sup>1</sup><sup>8</sup></span>, 1 ≤ X ≤ <span class="tex-math-text">10<sup>1</sup><sup>8</sup></span>). 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выходной файл должен содержать одно целое число — искомое количество дней. </p></span></div>
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
            <td>1 2 1 3 10</td>
            <td>8</td>
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
            <td>1 2 1 3 11</td>
            <td>9</td>
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
            <td>19 3 14 6 113</td>
            <td>4</td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Рассмотрим пример: </p></span><p>2 4 3 3 25 </p>
      <p>7 </p>
      <p>В приведенном примере лесорубы вырубают 25 деревьев за 7 дней следующим образом: </p>
      <p>* 1-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 5 деревьев; </p>
      <p>* 2-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 10 деревьев; </p>
      <p>* 3-й день: Дмитрий срубает 2 дерева, Федор отдыхает, итого 12 деревьев; </p>
      <p>* 4-й день: Дмитрий отдыхает, Федор срубает 3 дерева, итого 15 деревьев; </p>
      <p>* 5-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 20 деревьев; </p>
      <p>* 6-й день: Дмитрий срубает 2 дерева, Федор отдыхает, итого 22 дерева; </p>
      <p>* 7-й день: Дмитрий срубает 2 дерева, Федор срубает оставшееся 1 дерево, итого все 25 деревьев срублены. </p>
      <p>Внимание! Тест из примера не подходит под ограничения для подзадач 2 и 3, но решение принимается на проверку только в том
         случае, если оно выводит правильный ответ на тесте из примера. Решение должно выводить правильный ответ на тест даже, если
         оно рассчитано на решение только каких-либо из подзадач 2 и 3 
      </p>
   </div>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Покрытие K отрезками</h1>
   </div>
   <div class="legend"> Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины l. Найдите минимальное l.
      </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> На первой строке n<span class="tex-math-text">(1 &le; n &le; 10<sup>5</sup>)</span> и
    <math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> (<!--l. 52--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <mi>k</mi> <mo>≤</mo> <mi>n</mi></math>).
  На второй n чисел <span class="tex-math-text">x<sub>i</sub> (|x<sub>i</sub>| &le; 10<sup>9</sup>)</span>. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Минимальное такое l, что точки можно покрыть k отрезками длины l.
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>6 2<br>1 2 3 9 8 7</td>
            <td>2</td>
         </tr>
      </tbody>
   </table>
</div>
