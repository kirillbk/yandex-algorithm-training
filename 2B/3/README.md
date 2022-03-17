<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Количество совпадающих</h1>
   </div>
   <div class="legend"><span style="">
         <p>Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел содержится одновременно как
            в первом списке, так и во втором. Примечание. Эту задачу на Питоне можно решить в одну строчку. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводятся два списка чисел. Все числа каждого списка находятся на отдельной строке. </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите ответ на задачу. </p></span></div>
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
            <td>1 3 2<br>4 3 2</td>
            <td>2</td>
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
            <td>1 2 6 4 5 7<br>10 2 3 4 8</td>
            <td>2</td>
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
            <td>1 7 3 8 10 2 5<br>6 5 2 8 4 3 7</td>
            <td>5</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Встречалось ли число раньше</h1>
   </div>
   <div class="legend"><span style="">
         <p>Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке),
            если это число ранее встречалось в последовательности или NO, если не встречалось. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводится список чисел. Все числа списка находятся на одной строке. </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите ответ на задачу. </p></span></div>
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
            <td>1 2 3 2 3 4</td>
            <td>NO<br>NO<br>NO<br>YES<br>YES<br>NO</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Уникальные элементы</h1>
   </div>
   <div class="legend"><span style="">
         <p>Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке,
            в котором они встречаются в списке. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводится список чисел. Все числа списка находятся на одной строке. </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите ответ на задачу. </p></span></div>
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
            <td>1 2 2 3 3 3</td>
            <td>1</td>
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
            <td>4 3 5 2 5 1 3 5</td>
            <td>4 2 1</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Угадай число</h1>
   </div>
   <div class="legend"><span style="">
         <p>Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого
            она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное
            или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие
            ответы получила и просит вас помочь ей определить, какие числа мог задумать Август. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входных данных содержит число n&nbsp;— наибольшее число, которое мог загадать Август. Далее идут строки, содержащие
            вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами. После каждой строки с вопросом идет
            ответ Августа: YES или NO. Наконец, последняя строка входных данных содержит одно слово HELP. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август. </p></span></div>
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
            <td>10<br>1 2 3 4 5<br>YES<br>2 4 6 8 10<br>NO<br>HELP</td>
            <td>1 3 5</td>
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
            <td>10<br>1 2 3 4 5 6 7 8 9 10<br>YES<br>1<br>NO<br>2<br>NO<br>3<br>NO<br>4<br>NO<br>6<br>NO<br>7<br>NO<br>8<br>NO<br>9<br>NO<br>10<br>NO<br>HELP</td>
            <td>5</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Автомобильные номера</h1>
   </div>
   <div class="legend"><span style="">
         <p>Неизвестный водитель совершил ДТП и скрылся с места происшествия. Полиция опрашивает свидетелей. Каждый из них говорит, что
            запомнил какие-то буквы и цифры номера. Но при этом свидетели не помнят порядок этих цифр и букв. Полиция хочет проверить
            несколько подозреваемых автомобилей. Будем говорить, что номер согласуется с показанием свидетеля, если все символы, которые
            назвал свидетель, присутствуют в этом номере (не важно, сколько раз).
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала задано число M <= 100 - количество свидетелей. Далее идет <span class="tex-math-text">M</span> строк, каждая из которых описывает показания очередного свидетеля. Эти строки непустые и состоят из не более чем 20 символов.
            Каждый символ в строке - либо цифра, либо заглавная латинская буква, причём символы могут повторяться. <br> 
         </p></span><p>Затем идёт число N <= 1000 - количество номеров. Следующие строки представляют из себя номера подозреваемых машин и имеют такой же формат, как и показания
         свидетелей.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выпишите номера автомобилей, согласующиеся с максимальным количеством свидетелей. Если таких номеров несколько, то выведите
            их в том же порядке, в котором они были заданы на входе.
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
            <td>3<br>ABC<br>A37<br>BCDA<br>2<br>A317BD<br>B137AC</td>
            <td>B137AC</td>
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
            <td>2<br>1ABC<br>3A4B<br>3<br>A143BC<br>C143AB<br>AAABC1<br></td>
            <td>A143BC<br>C143AB</td>
         </tr>
      </tbody>
   </table>
</div>
