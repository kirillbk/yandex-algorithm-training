<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Толя-Карп и новый набор структур, часть 2</h1>
   </div>
   <div class="legend"><span style="">
         <p>Толя-Карп запросил для себя <span class="tex-math-text">n</span> посылок с &laquo;Аллигатор-экспресс&raquo;.
         </p></span><p>Посылка представляет из себя ящик. Внутри ящика лежит целое число <span class="tex-math-text">a<sub>i</sub></span>. Номер на ящике <span class="tex-math-text">d<sub>i</sub></span> указывает на цвет числа, лежащего внутри. 
      </p>
      <p>Толю-Карпа интересует, чему будут равны значения чисел, если сложить между собой все те, что имеют одинаковый цвет. Напишите,
         пожалуйста, программу, которая выводит результат.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке одно число <span class="tex-math-text">n</span> (<span class="tex-math-text">0 &le; n &le; 2*10<sup>5</sup></span>).
         </p></span><p>В следующих <span class="tex-math-text">n</span> строках заданы по два числа: цвет числа в ящике <span class="tex-math-text">d<sub>i</sub></span> и значение числа <span class="tex-math-text">a<sub>i</sub></span> (<span class="tex-math-text">-10<sup>18</sup> &le; d<sub>i</sub>, a<sub>i</sub> &le; 10<sup>18</sup></span>).
      </p>
      <p>Гарантируется, что сумма чисел одного цвета не превышает <span class="tex-math-text">10<sup>18</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите в порядке возрастания <span style="font-weight:bold;">номера цвета</span> пары чисел, каждая в новой строке: номер цвета и сумму всех чисел данного цвета.
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
            <td>7<br>1 5<br>10 -5<br>1 10<br>4 -2<br>4 3<br>4 1<br>4 0</td>
            <td>1 15<br>4 2<br>10 -5</td>
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
            <td>5<br>5 -10000<br>-5 100000000000<br>10 2000000000000<br>-5 -300000000000<br>0 10000000000000</td>
            <td>-5 -200000000000<br>0 10000000000000<br>5 -10000<br>10 2000000000000</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Выборы в США</h1>
   </div>
   <div class="legend"><span style="">
         <p>Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала проводятся выборы
            в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы: на этих выборах
            каждый штат имеет определенное число голосов&nbsp;— число выборщиков от этого штата. На практике, все выборщики от штата голосуют
            в соответствии с результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты,
            имеющие различное число голосов. Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом.
            Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата, затем через пробел
            идет количество выборщиков, отдавших голоса за этого кандидата. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них голосов. </p></span></div>
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
            <td>McCain 10<br>McCain 5<br>Obama 9<br>Obama 8<br>McCain 1</td>
            <td>McCain 16<br>Obama 17</td>
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
            <td>ivanov 100<br>ivanov 500<br>ivanov 300<br>petr 70<br>tourist 1<br>tourist 2</td>
            <td>ivanov 900<br>petr 70<br>tourist 3</td>
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
            <td>bur 1</td>
            <td>bur 1</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Частотный анализ</h1>
   </div>
   <div class="legend"><span style="">
         <p>Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию
            их количества появления в тексте, а при одинаковой частоте появления&nbsp;— в лексикографическом порядке. Указание. После того,
            как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова. Желаемого можно добиться,
            если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово. Например,
            <span style="">[(2, 'hi'), (1, 'what'), (3, 'is')]</span>. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если
            они равны&nbsp;— то по второму. Это почти то, что требуется в задаче. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводится текст. </p></span></div>
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
            <td>hi<br>hi<br>what is your name<br>my name is bond<br>james bond<br>
             my name is damme<br>van damme<br>claude van damme<br>jean claude van damme</td>
            <td>damme<br>is<br>name<br>van<br>bond<br>claude<br>hi<br>my<br>james<br>jean<br>what<br>your</td>
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
            <td>oh you touch my tralala<br>mmm my ding ding dong</td>
            <td>ding<br>my<br>dong<br>mmm<br>oh<br>touch<br>tralala<br>you</td>
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
         <tr><td>ai ai ai ai ai ai ai ai ai ai</td>
         <td>ai</td>
        </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Выборы Государственной Думы</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации” определяет следующий
            алгоритм пропорционального распределения мест в парламенте. 
         </p></span><p>Необходимо распределить 450 мест между партиями, участвовавших в выборах. Сначала подсчитывается сумма голосов избирателей,
         поданных за каждую партию и подсчитывается сумма голосов, поданных за все партии. Эта сумма делится на 450, получается величина,
         называемая “первое избирательное частное” (смысл первого избирательного частного - это количество голосов избирателей, которое
         необходимо набрать для получения одного места в парламенте). 
      </p>
      <p>Далее каждая партия получает столько мест в парламенте, чему равна целая часть от деления числа голосов за данную партию на
         первое избирательное частное. 
      </p>
      <p>Если после первого раунда распределения мест сумма количества мест, отданных партиям, меньше 450, то оставшиеся места передаются
         по одному партиям, в порядке убывания дробной части частного от деления числа голосов за данную партию на первое избирательное
         частное. Если же для двух партий эти дробные части равны, то преимущество отдается той партии, которая получила большее число
         голосов. 
      </p>
      <p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На вход программе подается список партий, участвовавших в выборах. Каждая строка входного файла содержит название партии (строка,
            возможно, содержащая пробелы), затем, через пробел, количество голосов, полученных данной партией – число, не превосходящее
            <span class="tex-math-text">10<sup>8</sup></span>. 
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Программа должна вывести названия всех партий и количество голосов в парламенте, полученных данной партией. Названия необходимо
            выводить в том же порядке, в котором они шли во входных данных. 
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
            <td>Party One 100000<br>Party Two 200000<br>Party Three 400000<br></td>
            <td>Party One 64<br>Party Two 129<br>Party Three 257<br></td>
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
            <td>Party number one 100<br>Partytwo 100</td>
            <td>Party number one 225<br>Partytwo 225<br></td>
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
            <td>Party number one 449<br>Partytwo 1</td>
            <td>Party number one 449<br>Partytwo 1</td>
         </tr>
      </tbody>
   </table>
</div>

<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Форум</h1>
   </div>
   <div class="legend"><span style="">
         <p>Клуб Юных Хакеров организовал на своем сайте форум. Форум имеет следующую структуру: каждое сообщение либо начинает новую
            тему, либо является ответом на какое-либо предыдущее сообщение и принадлежит той же теме.
         </p></span><p>После нескольких месяцев использования своего форума юных хакеров заинтересовал вопрос - какая тема на их форуме наиболее
         популярна. Помогите им выяснить это.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится целое число N - количество сообщений в форуме (1 &lt;= N &lt;= 1000). Следующие строки содержат описание
            сообщений в хронологическом порядке.
         </p></span><p>Описание сообщения, которое представляет собой начало новой темы, состоит из трех строк. Первая строка содержит число 0. Вторая
         строка содержит название темы. Длина названия не превышает 30 символов. Третья строка содержит текст сообщения.
      </p>
      <p>Описание сообщения, которое является ответом на другое сообщение, состоит из двух строк. Первая строка содержит целое число
         - номер сообщения, ответом на которое оно является. Сообщения нумеруются, начиная с единицы. Ответ всегда появляется позже,
         чем сообщение, ответом на которое он является. Вторая строка содержит текст сообщения.
      </p>
      <p>Длина каждого из сообщений не превышает 100 символов.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите название темы, к которой относится наибольшее количество сообщений. Если таких тем несколько, то выведите первую
            в хронологическом порядке
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
            <td>7<br>0<br>Олимпиада по информатике<br>Скоро третья командная олимпиада?<br>
            0<br>Новая компьютерная игра<br>Вышла новая крутая игра!<br>
            1<br>Она пройдет 24 ноября<br>
            1<br>В Санкт-Петербурге и Барнауле<br>
            2<br>Где найти?<br>
            4<br>Примет участие более 50 команд<br>
            6<br>Интересно, какие будут задачи</td>
            <td>Олимпиада по информатике</td>
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
            <td>1<br>0<br>topic 1<br>body 1<br></td>
            <td>topic 1</td>
         </tr>
      </tbody>
   </table>
</div>
