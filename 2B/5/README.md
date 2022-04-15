<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Префиксные суммы</h1>
   </div>
   <div class="legend"> В этой задаче вам нужно будет много раз отвечать на запрос «Найдите сумму чисел на отрезке в массиве». </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке записано два целых числа n и q <span class="tex-math-text"> ( 1 &le; n,q &le; 3*10<sup>5</sup>)</span>
      - размер массива и количество запросов. <!--l. 52-->
      <p style="text-indent: 0em;">Во второй строке записаны n целых чисел <span class="tex-math-text">a<sub>i</sub> (1 &le; a<sub>i</sub> &le; 10<sup>9</sup>)</span>
      - сам массив. <!--l. 54-->
      </p><p style="text-indent: 0em;">Далее в <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>
      строках описаны запросы к массиву. Каждый запрос описывается двумя числами <!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math>, <!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> (<!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <mi>l</mi> <mo>≤</mo> <mi>r</mi> <mo>≤</mo> <mi>n</mi></math>)
      - левой и правой границей отрезка, на котором нужно найти сумму. </p>
      <p></p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Для каждого запроса в отдельной строке выведите единственное число - сумму на соответствующем отрезке. </div>
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
            <td>4 10<br>
              1 2 3 4<br>
              1 1<br>
              1 2<br>
              1 3<br>
              1 4<br>
              2 2<br>
              2 3<br>
              2 4<br>
              3 3<br>
              3 4<br>
              4 4
            </td>
            <td>1<br>3<br>6<br>10<br>2<br>5<br>9<br>3<br>7<br>4</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Максимальная сумма</h1>
   </div>
   <div class="legend"> В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой. </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных записано единственное число n <span class="tex-math-text">a<sub>i</sub> (1 &le; n &le; 3 * 10<sup>5</sup>)</span> - размер массива. <!--l. 52-->
      <p style="text-indent: 0em;">Во второй строке записано n целых чисел <span class="tex-math-text">a<sub>i</sub> (-10<sup>9</sup> &le; a<sub>i</sub> &le; 10<sup>9</sup>)</span>
      - сам массив. </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно число - максимальную сумму на отрезке в данном массиве. </div>
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
            <td>10</td>
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
            <td>4<br>5 4 -10 4</td>
            <td>9</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Каждому по компьютеру</h1>
   </div>
   <div class="legend"><span style="">
         <p>В новом учебном году на занятия в компьютерные классы Дворца Творчества Юных пришли учащиеся, которые были разбиты на N групп.
            В i-й группе оказалось <span class="tex-math-text">X<sub>i</sub></span> человек. Тут же перед директором встала серьезная проблема: как распределить группы по аудиториям. Во дворце имеется M ≥
            N аудиторий, в j-й аудитории имеется <span class="tex-math-text">Y<sub>j</sub></span> компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер и еще один компьютер был у преподавателя. Переносить
            компьютеры из одной аудитории в другую запрещается. Помогите директору!
         </p></span><p>Напишите программу, которая найдет, какое максимальное количество групп удастся одновременно распределить по аудиториям, чтобы
         всем учащимся в каждой группе хватило компьютеров, и при этом остался бы еще хотя бы один для учителя.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На первой строке входного файла расположены числа N и M (1 ≤ N ≤ M ≤ 1000). На второй строке расположено N чисел — <span class="tex-math-text">X<sub>1</sub></span>, …, <span class="tex-math-text">X<sub>N</sub></span> (1 ≤ <span class="tex-math-text">X<sub>i</sub></span> ≤ 1000 для всех 1 ≤ i ≤ N). На третьей строке расположено M чисел <span class="tex-math-text">Y<sub>1</sub></span>, ..., <span class="tex-math-text">Y<sub>M</sub></span> (1 ≤ <span class="tex-math-text">Y<sub>i</sub></span> ≤ 1000 для всех 1 ≤ i ≤ M).
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите на первой строке число P - количество групп, которые удастся распределить по аудиториям. На второй строке выведите
            распределение групп по аудиториям – N чисел, i-е число должно соответствовать номеру аудитории, в которой должна заниматься
            i-я группа. (Нумерация как групп, так и аудиторий, начинается с 1). Если i-я группа осталась без аудитории, i-е число должно
            быть равно 0. Если допустимых распределений несколько, выведите любое из них.
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
            <td>1 1<br>1<br>2</td>
            <td>1<br>1</td>
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
            <td>1 1<br>1<br>1</td>
            <td>0<br>0</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Правильная, круглая, скобочная</h1>
   </div>
   <div class="legend"><span style="">
         <p>Если из правильного арифметического выражения вычеркнуть всё, кроме круглых скобок, то получится правильная скобочная последовательность.
            Проверьте, является ли введённая строка правильной скобочной последовательностью.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводится непустая строка, состоящая из открывающих и закрывающих круглых скобок. Длина строки не превосходит 100000</p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите YES если введённая строка является правильной скобочной последовательностью и NO иначе</p></span></div>
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
            <td><pre>(())()</pre></td>
            <td><pre>YES
</pre></td>
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
            <td>(()))()</td>
            <td>NO</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Сумма трёх</h1>
   </div>
   <div class="legend"> Даны три массива целых чисел <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></math>
      и целое число <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>.
      <!--l. 49-->
      <p style="text-indent: 0em;">Найдите такие <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>,
      что <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>A</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>+</mo> <msub><mrow><mi>B</mi></mrow><mrow><mi>j</mi></mrow></msub> <mo>+</mo> <msub><mrow><mi>C</mi></mrow><mrow><mi>k</mi></mrow></msub>
      <mo>=</mo> <mi>S</mi></math>. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> На первой строке число S <span class="tex-math-text"> (1 &le; S &le; 10<sup>5</sup>)</span>. Следующие три строки
      содержат описание массивов <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></math>
      в одинаковом формате: первое число задает длину n соответствующего массива <span class="tex-math-text"> ( 1 &le; n &le; 15000)</span>,
      затем заданы n целых чисел от 1 до <span class="tex-math-text">10<sup>9</sup></span> — сам массив. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Если таких <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>
      не существует, выведите единственное число -1. Иначе выведите на одной строке три числа — <!--l. 59--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>. Элементы массивов
      нумеруются с нуля. Если ответов несколько, выведите лексикографически минимальный. 
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
            <td>3<br>2 1 2<br>2 3 1<br>2 3 1</td>
            <td>0 1 1</td>
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
            <td>10<br>1 5<br>1 4<br>1 3</td>
            <td>-1</td>
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
            <td>5<br>
            4 1 2 3 4<br>
            3 5 2 1<br>
            4 5 3 2 2<br>
            </td>
            <td>0 1 2</td>
         </tr>
      </tbody>
   </table>
</div>
