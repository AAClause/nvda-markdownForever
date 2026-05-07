---
author:
- Đặng Mạnh Cường &lt;<dangmanhcuong@gmail.com>&gt;
autonumber-headings: 1
css:
- style.css
date: Thứ bảy, 05/09/2020
extratags: 1
extratags-back: 0
filename: doc_vi
include-after:
- '%addonDir%/doc/dependencies.md'
keywords: tài liệu, MarkdownForever, NVDA add-on, tiếng Việt
lang: vi
langd: vi
subtitle: Bộ chuyển đổi Markdown và HTML đầy đủ tính năng cho NVDA
template: default
title: Tài liệu hướng dẫn sử dụng MarkdownForever %addonVersion%
toc: 1
...

**Mục lục**
%toc%

## Giới thiệu

MarkdownForever là một add-on nhỏ cho NVDA, dùng để chuyển đổi nội dung Markdown hay HTML một cách dễ dàng. Chỉ việc viết hoặc cho hiển thị bất cứ nội dung nào ở định dạng Markdown hay HTML và bấm một phím tắt đơn giản để chuyển đổi hoặc xem trước kết quả một cách nhanh chóng bất cứ lúc nào, hoàn toàn đúng như khi nó hiển thị trên trang web của bạn, hay dạng mã nguồn HTML, sẵn sàng để dán ở bất cứ nơi nào có hỗ trợ HTML.

MarkdownForever có thể:

* Chuyển đổi Markdown thành HTML
* Chuyển đổi Markdown thành mã nguồn HTML
* Chuyển đổi HTML thành Markdown
* Chuyển đổi Markdown thành định dạng HTML

## Nhưng Markdown là gì?

Theo Wikipedia,

> Markdown là một ngôn ngữ đánh dấu với cú pháp văn bản thô, được thiết kế để có thể dễ dàng chuyển thành HTML và nhiều định dạng khác sử dụng một công cụ cùng tên. Nó thường được dùng để tạo các tập tin readme, viết tin nhắn trên các diễn đàn, và tạo văn bản có định dạng bằng một trình biên tập văn bản thô.

Bạn có thể tìm hiểu thêm về Markdown bằng cách đọc [bài viết đầy đủ trên Wikipedia.](https://vi.wikipedia.org/wiki/Markdown)

Như vậy, thay vì viết tài liệu web bằng HTML với nguy cơ bị lỗi, bạn sẽ dùng các thẻ dễ nhớ hơn và công việc của bạn sẽ hoàn thành nhanh chóng. Với Markdown, bạn sẽ làm được ít nhiều những gì  HTML có thể làm: tiêu đề, danh sách có thứ tự (số đếm) hoặc không thứ tự (các dấu đầu dòng), liên kết, thậm chí là bảng biểu.

Ví dụ, muốn làm tiêu đề cấp 1, bạn sẽ viết một dấu thăng (#), sau đó là tên của tiêu đề, có hoặc không có khoảng trắng giữa chúng:

> `#Đây là ví dụ về tiêu đề cấp 1`

sẽ hiển thị trong tài liệu HTML của bạn như sau:

> <h1>\!Đây là ví dụ về tiêu đề cấp 1</h1>

Với tiêu đề cấp 2, bạn sẽ dùng hai dấu thăng, ba dấu cho tiêu đề cấp 3, v...v...
 
Bây giờ, hãy làm một danh sách không thứ tự. để làm điều này, bạn có thể thêm dấu sao (*) vào trước mỗi thành phần trong danh sách. Xem ví dụ sau:

<blockquote>

```
* Cam
* Đường
* Sữa
```

</blockquote>

Sẽ hiển thị:

> * Cam
> * Đường
> * Sữa

Bạn cũng có thể tạo một liên kết bằng cách đặt tiêu đề của liên kết đó trong cặp dấu ngoặc vuông ([]). Sau đó, đặt đường dẫn liên kết trong cặp dấu ngoặc tròn và không có khoảng trắng. Ví dụ:

    [Bấm vào đây để mở trang web của  NVAccess](https://www.nvaccess.org)

sẽ cho ra:

[Bấm vào đây để mở trang web của  NVAccess](https://www.nvaccess.org)
 
Thậm chí, bạn có thể `*in nghiêng một đoạn văn bản*` bằng cách đặt nó trong hai dấu sao, hoặc `**in đậm văn bản**` bằng cách đặt nó vào hai cặp dấu sao... Và còn nhiều cái khác nữa. Xem [Bài viết sau](https://www.markdownguide.org/cheat-sheet/) để biết thêm chi tiết.

## Chuyển đổi Markdown thành HTML

Tính năng này cho phép bạn chuyển nội dung Markdown hiển thị trên màn hình thành HTML, hiển thị như cách mà nội dung  Markdown của bạn sẽ thể hiện ở tài liệu HTML. Đây có thể là một tài liệu được viết ở định dạng Markdown, một tập tin .md có sẵn trên ổ cứng hoặc một nội dung Markdown tìm thấy trên một trang web. Mặc định, MarkdownForever sẽ chuyển tất cả nội dung đang hiển thị, nhưng bạn cũng có thể chọn một đoạn nhất định để chuyển đổi.

Bạn có thể dùng các phím lệnh sau:

- *NVDA+ALT+b*: kết quả hiển thị dưới dạng trang web trên trình duyệt web mặc định của bạn.
- *NVDA+ALT+n*: kết quả hiển thị dưới dạng trang web  trên màn hình ảo của NVDA.

Xin lưu ý rằng lựa chọn hiển thị trên trình duyệt được khuyên dùng thay cho việc hiển thị trên màn hình ảo của NVDA. Một số thẻ, cụ thể là thẻ  HTML5 như `<details>,` chưa được hỗ trợ trên màn hình ảo.

## Chuyển đổi Markdown thành mã nguồn HTML

Tính năng này chuyển đổi nội dung Markdown thành ngôn ngữ HTML thuần túy. Khi hoàn tất, bạn có thể chép và dán vào tập tin HTML, vào bài viết trên diễn đàn, hoặc mỗi vùng nhập liệu trên web có hỗ trợ mã HTML.

Sử dụng các phím lệnh sau:

- *NVDA+ALT+l*: kết quả hiển thị trên màn hình ảo của NVDA.
- *NVDA+Ctrl+h*: Chép mã nguồn HTML vào bộ nhớ tạm.

## Chuyển đổi HTML thành Markdown

Tính năng này cố gắng tạo ra một văn bản Markdown từ nguồn nội dung HTML. Thông thường, nó xử lý toàn bộ nội dung hiển thị trên màn hình hoặc một đoạn nào đó được chọn. Sử dụng các phím lệnh sau:

- *NVDA+Alt+k*: hiển thị kết quả trên màn hình ảo của NVDA.
- *NVDA+Shift+g*: chép kết quả vào bộ nhớ tạm.

Bạn cũng có thể chuyển đổi một trang  HTML thành Markdown bằng cách đơn giản là chọn đường dẫn của nó. Tuy nhiên, bạn phải chắc chắn là bộ chuyển đổi HTML2Text phải được chọn làm mặc định trong [Cài đặt của MarkdownForever,](#thiet-lap-mac-inh-cua-markdownforever) trong phần tùy chỉnh của NVDA.
 
## Chuyển đổi Markdown thành định dạng HTML

Chức năng này chuyển đổi nội dung Markdown của bạn thành định dạng HTML và chép nó vào bộ nhớ tạm. Định dạng HTML sẽ giống như mọi trang web hiển thị trên trình duyệt của bạn, với các liên kết có thể click, tiêu đề, v...v... Điều này chỉ có thể thực hiện được từ nội dung Markdown chứ không làm được với mã nguồn HTML. Để làm điều này, bấm NVDA+Shift+h.

Lưu ý rằng *định dạng HTML* có thể dán vào các ứng dụng như Microsoft Word, Wordpad, Thunderbird, vài ô nhập liệu trên trang web, v...v... Tuy nhiên, không thể dán nó vào các trình soạn thảo như Notepad, Notepad++, v...v...

## Chế độ tương tác

Chế độ tương tác là một chức năng dùng để trình bày tất cả tính năng của MarkdownForever trong một hộp thoại, cung cấp cho bạn các tính năng bổ sung tiện lợi hơn. Để mở chế độ này, bấm NVDA+CTRL+i.
Sau đây là mô tả màn hình của tính năng, theo cách duyệt bằng Tab:

* "Chuyển đổi thành": hộp xổ đầu tiên này cho phép bạn chọn cách chuyển đổi: HTML, Mã nguồn HTML hoặc Markdown. Dùng các phím mũi tên lên xuống để chọn.
* "Tạo mục lục": Hộp kiểm này sẽ cho phép bạn chọn tạo hay không tạo mục lục của các chương trong tài liệu  HTML của bạn với liên kết có thể click để đi đến chương đó. Trạng thái của tùy chọn này cũng có thể thiết lập mặc định trong [Cài đặt MarkdownForever.](#thiet-lap-mac-inh-cua-markdownforever)
* "Cố gắng đánh số tự động cho tiêu đề": nếu chọn, Markdown Forever sẽ cố gắng thêm số vào trước mỗi tiêu đề (hay chương), tùy theo cấp độ của mỗi tiêu đề. Ví dụ: "1." cho tiêu đề cấp 1, "1.1." cho tiêu đề cấp 2, v...v... 
* "Bật các thẻ bổ sung": Nếu chọn, sẽ cho phép sử dụng [các thẻ đặc biệt](#cac-the-bo-sung) trong nội dung Markdown của bạn để tự chèn những thứ như ngày giờ hiện tại. Trạng thái của tùy chọn này cũng có thể thiết lập mặc định trong [Cài đặt MarkdownForever.](#thiet-lap-mac-inh-cua-markdownforever)
* "Cho phép dịch ngược các thẻ bổ sung": tùy chọn này sẽ thể hiện có hay không việc [các thẻ bổ sung](#cac-the-bo-sung) sẽ được trả lại nguyên mẫu của nó (ví dụ: %date%) khi chuyển đổi nội dung HTML được tạo bởi Markdown Forever trở về Markdown. 
* "Tên": bạn có thể điền	 tên cho tài liệu HTML của bạn ở đây, và nó sẽ hiển thị trên trình duyệt.
* "Khối siêu dữ liệu tương ứng": ô có thuộc tính chỉ đọc này hiển thị 
* "Tạo siêu dữ liệu tương ứng từ mã nguồn HTML": khi chuyển đổi một  tập tin mã nguồn HTML thành Markdown, nó cố gắng đoán siêu dữ liệu từ mã nguồn (title - tên, lang - ngôn ngữ, filename -tên tập tin, v...v...) và tạo ra [khối siêu dữ liệu](#tuy-chon-khoi-sieu-du-lieu) cho bạn. Tùy chọn này chỉ có khi chuyển đổi HTML thành Markdown.
* "Hiển thị trên màn hình ảo": nút này sẽ hiện nội dung đã chuyển đổi của bạn trên màn hình ảo của NVDA.
* "Hiển thị trên trình duyệt": hiển thị nội dung đã chuyển đổi của bạn trên trình duyệt mặc định.
* "Chép vào bộ nhớ tạm": chép nội dung đã chuyển đổi của bạn vào bộ nhớ tạm của Windows, sẵn sàng để dán.
* "Lưu kết quả": sẽ yêu cầu bạn lưu tài liệu đã chuyển đổi vào ổ cứng thông qua một hộp thoại lưu tiêu chuẩn của Windows. Bạn cũng có thể thiết lập nơi lưu mặc định trong [Cài đặt MarkdownForever.](#thiet-lap-mac-inh-cua-markdownforever)

## Tùy chọn khối siêu dữ liệu

Khối siêu dữ liệu cho phép bạn thiết lập vài tham số nhất định cho một tài liệu cụ thể, độc lập với [các thiết lập mặc định.](#thiet-lap-mac-inh-cua-markdownforever) Chúng phải được đặt ở đầu tài liệu và phải bắt đầu với ba dấu trừ ("---") và kết thúc với ba dấu chấm ("...") hoặc ba dấu trừ ("---"). Mỗi thành phần phải được nhập theo mẫu: khóa: "giá trị" (giá trị phải được đặt trong dấu ngoặc kép). Phải đặt một dòng trắng tiếp sau khối siêu dữ liệu.

### Danh sách siêu dữ liệu được hỗ trợ

* author (hoặc authors): ghi ra tên của một hay nhiều tác giả cho tài liệu (xem ví dụ bên dưới). Thông tin này sẽ được thêm vào phần đầu của tập tin HTML. Khóa này không phân biệt chữ hoa / thường.
* autonumber-headings: xác định có hay không có việc tự đánh số cho tiêu đề. Có các giá trị: true (1) tức là có hoặc false (0) tức là không.
* css (hoặc CSS): chỉ ra một hoặc nhiều  tập tin CSS để  trình bày tài liệu của bạn (xem ví dụ bên dưới). Khóa này không phân biệt chữ hoa / thường.
* date: ghi ra ngày tháng cho tài liệu của bạn. Thông tin này sẽ được thêm vào phần đầu của tập tin HTML.
* extratags: chỉ định có hay không việc thông dịch [các thẻ bổ sung](#cac-the-bo-sung). Có các giá trị: true (1) tức là có hoặc false (0) tức là không.
* extratags-back: xác định có hay không việc dịch ngược  [các thẻ bổ sung](#cac-the-bo-sung) về nguyên mẫu của nó (ví dụ: %date%) khi chuyển đổi một nội dung HTML được tạo bởi Markdown Forever về Markdown. Có các giá trị: true (1) tức là có hoặc false (0) tức là không.
* filename: quy định tên của tập tin khi lưu lại.
* keywords: quy định các từ khóa liên quan đến những chủ đề được nói đến trong tài liệu của bạn.
* lang: quy định ngôn ngữ chính cho tài liệu. Nếu cần, hãy dùng các thẻ span/div với thuộc tính lang để xác định các thay đổi ngôn ngữ, ngay bên trong tài liệu.
* mathjax: xác định có hay không việc  chuyển đổi các công thức toán viết bằng [LaTeX](https://vi.wikipedia.org/wiki/LaTeX). Có các giá trị: true (1) tức là có hoặc false (0) tức là không. Yêu cầu có kết nối mạng và bạn phải mở kết quả được chuyển đổi trên trình duyệt để hiển thị nó một cách chính xác, vì nội dung LaTeX được thông dịch không thể xuất ra màn hình ảo của NVDA.
[Bấm vào đây để biết thêm thông tin về MathJax.](http://docs.mathjax.org/en/latest/)
* path: chỉ ra thư mục để lưu tài liệu. Có hỗ trợ các biến môi trường %userprofile%, %appdata% và %tmp%.
* subtitle:  ghi ra tên phụ cho tài liệu HTML của bạn. Thông tin này sẽ được thêm vào phần đầu của tập tin HTML.
* title: ghi ra tên của tài liệu HTML. Trong chế độ tương tác, ô tên sẽ được điền tự động bằng giá trị của khóa này.
* toc: xác định có hay không việc tạo mục lục. Có các giá trị: true (1) tức là có hoặc false (0) tức là không.

### Ví dụ về việc dùng siêu dữ liệu
<blockquote>

```
---
title: "Đặt một tên đơn giản"
date: 2019-11-08
subtitle: "Điền tên phụ cho tài liệu của bạn"
lang: vi
author:
- John Doe
- David Murphy
CSS:
- %userprofile%/document/main.css
- %userprofile%/document/custom.css
keywords: NVDA, Markdown, HTML
filename: test
path: "%userprofile%/desktop"
toc: 0
autonumber-headings: 1
mathjax: 0
---

Xin chào thế giới! <span lang="en"Hello world!</span> <span lang="fr">Bonjour le monde !</span> <span lang="es">¡Hola mundo!</span>
```

</blockquote>

Trong ví dụ ở trên, nội dung sẽ được đọc thành tiếng của bốn ngôn ngữ, xem như bộ đọc bạn đang dùng có hỗ trợ tự chuyển ngôn ngữ và đã đánh dấu tùy chọn tương ứng trong cài đặt tiếng nói của  NVDA. Nó sẽ đọc như sau:

Xin chào thế giới! <span lang="en"Hello world!</span> <span lang="fr">Bonjour le monde !</span> <span lang="es">¡Hola mundo!</span>

## Các thẻ bổ sung

Thẻ bổ sung là những bộ giữ chỗ đặc biệt mà bạn có thể đặt vào nội dung Markdown của mình để tự thêm các thông tin hệ thống như ngày giờ hiện tại, sẽ được tạo ra ở dạng văn bản trong tài liệu HTML của bạn.

### Các thẻ bổ sung được hỗ trợ

| **Trong nội dung Markdown** | **Giải thích** | **Kết quả trên trình duyệt** |
| :----------: | :----------: | :----------: |
| `%date%` | Ngày hiện tại | %date% |
| `%time%` | Giờ hiện tại | %time% |
| `%now%` | Ngày / giờ hiện tại | %now% |
| `%day%` | Ngày hiện tại (định dạng viết dài) | %day% |
| `%dday%` | Ngày hiện tại (định dạng số) | %dday% |
| `%month%` | Tháng (định dạng viết dài) | %month% |
| `%dmonth%` | Tháng hiện tại (định dạng số) | %dmonth% |
| `%year%` | Năm hiện tại (hai chữ số) | %year% |
| `%Year%` | Năm hiện tại (bốn chữ số) | %Year% |
| `%toc%` | Mục lục tại vị trí con trỏ (nếu bật thông qua siêu dữ liệu hoặc cài đặt mặc định) | N/A |

## Thiết lập mặc định của MarkdownForever

Có thể truy cập chúng từ trình đơn NVDA -> Cài đặt MarkdownForever -> Cài đặt và bạn sẽ có thể đặt mặc định nhiều thiết lập liên quan tới quá trình chuyển đổi đã đề cập ở trên:

* "Tạo mục lục": tùy chọn này cho phép bạn tạo hay không tạo một mục lục các chương của tài liệu HTML với liên kết dẫn tới mỗi chương. Lựa chọn này cũng có thể thiết lập trên một tài liệu cụ thể bằng cách dùng khóa "toc" trong phần [tùy chọn khối siêu dữ liệu](#tuy-chon-khoi-sieu-du-lieu) và đặt ở bất cứ đâu bằng cách dùng [các thẻ bổ sung tương ứng.](#cac-the-bo-sung)
* "Bật các thẻ bổ sung": nếu chọn,, nó sẽ bật khả năng sử dụng [các thẻ đặc biệt](#cac-the-bo-sung) trong nội dung Markdown của bạn để tự chèn những thứ như ngày giờ hiện tại. Lựa chọn này cũng có thể thiết lập trên một tài liệu cụ thể bằng cách dùng khóa các thẻ bổ sung trong [tùy chọn khối siêu dữ liệu.](#tuy-chon-khoi-sieu-du-lieu)
* "Tạo siêu dữ liệu tương ứng từ mã nguồn HTML": khi chuyển đổi một tập tin mã nguồn HTML qua Markdown, nó sẽ cố gắng đoán siêu dữ liệu từ mã nguồn (title - tên, lang - ngôn ngữ, filename - tên tập tin, v...v...) và tạo ra [khối siêu dữ liệu](#tuy-chon-khoi-sieu-du-lieu) cho bạn.
* "Hành động mặc định trong chế độ tương tác": cho phép chọn hành động mặc định sẽ được thực hiện khi bấm phím Enter trong [Chế độ tương tác:](#che-o-tuong-tac) hiển thị nội dung đã tạo trên trình duyệt, trên màn hình ảo hay chép vào bộ nhớ tạm.
* "Bộ công cụ Markdown": MarkdownForever cho phép bạn chọn giữa hai bộ chuyển đổi, [HTML2Text](https://pypi.org/project/html2text/) và [HTML2Markdown.](https://pypi.org/project/html2markdown/) Chỉ việc thử nghiệm và chọn cái nào bạn thích, căn cứ trên nhu cầu của bạn hoặc kết quả cho ra.
* "Tiện ích mở rộng Markdown": cấu hình các tính năng được `markdown-it-py` hỗ trợ (bảng, danh sách công việc, chú thích cuối trang, ID tiêu đề, v.v.).
* "Đường dẫn": tại đây bạn có thể thiết lập nơi lưu mặc định trên ổ đĩa cho các tài liệu đã chuyển đổi. Nó có ích nếu bạn luôn dùng một thư mục để lưu tất cả công việc của mình.
* "Quản lý mẫu HTML": sẽ mở một hộp thoại cho phép thêm, chỉnh sửa và xóa các mẫu HTML. Với mẫu, bạn sẽ có thể tùy chỉnh về mặt hình thức của tài liệu HTML bằng CSS (cascading styles sheets), ngôn ngữ đáng tin cậy cho kiểu dáng trang. Nó cho phép bạn thay đổi màu, bố cục hoặc thêm hình ảnh vào sản phẩm của bạn và tạo mẫu cho mọi nhu cầu cụ thể. Tất nhiên, có nhiều hướng dẫn học CSS trên web và [cái này](https://www.htmldog.com/guides/css/beginner/) có thể là tài liệu tốt để bắt đầu.

## Tổng hợp phím lệnh

- *NVDA+CTRL+i*: chế độ tương tác.
- *NVDA+ALT+b*: chuyển đổi Markdown thành HTML. Kết quả hiển thị trên trình duyệt mặc định.
- *NVDA+ALT+n*: chuyển đổi Markdown thành HTML. Kết quả hiển thị trên màn hình ảo của NVDA.
- *NVDA+ALT+k*: chuyển đổi HTML thành Markdown. Kết quả hiển thị trên màn hình ảo của NVDA.
- *NVDA+ALT+l*: chuyển đổi Markdown thành mã nguồn HTML. Kết quả hiển thị trên màn hình ảo của NVDA.
- *NVDA+SHIFT+g*: chuyển đổi HTML thành Markdown. Kết quả được chép vào bộ nhớ tạm.
- *NVDA+SHIFT+h*: chuyển đổi Markdown thành định dạng HTML . kết quả được chép vào bộ nhớ tạm.
- *NVDA+CTRL+h*: chuyển đổi Markdown thành mã nguồn HTML. Kết quả được chép vào bộ nhớ tạm.

## Thông tin Add-on

* Tác giả:
	- André &lt;<dev@andreabc.net>&gt;: người sáng lập và bảo trì chính của  add-on.
	- Sof &lt;<hellosof@gmail.com>&gt;: tài liệu hướng dẫn tiếng Anh và tiếng Pháp, nhiều gọi ý tính năng.
	- Victor Cai: Dịch ra tiếng Trung Quốc.
	- Çağrı Dogan, Umut Korkmaz: dịch ra tiếng Thổ Nhĩ Kỳ.
	- Rémy Ruiz &lt;<remyruiz@gmail.com>&gt;: dịch ra tiếng Tây Ban Nha.
	- Đặng Mạnh Cường &lt;<dangmanhcuong@gmail.com>&gt;: dịch ra tiếng Việt
	- Và còn nhiều nữa!
* Giấy phép: GNU General Public License, phiên bản 2
* Tải về [phiên bản chính thức](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon)
* Tải về [phiên bản thử nghiệm](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon?channel=dev)
* Kho chứa trên GitHub: [aaclause/NVDA-markdownForever](https://github.com/aaclause/nvda-markdownForever)
* **Các thư viện được bao gồm trong add-on**: