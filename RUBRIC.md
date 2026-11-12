# Tiêu chí đánh giá Day 3 — tối đa 100 điểm trong lớp

Trọng số giữ từ [starter Day 5](https://github.com/VinUni-AI20k/Day5-Segmentation-Data-Student) commit `3bff13d`. Task chưa nộp được ghi là chưa có bài nộp, không tự điền điểm giả. Học viên nộp link fork trên [LMS](https://aithucchien.vinuni.edu.vn) trước 12:00 trưa ngày hôm sau buổi lab (UTC+7). Bản nộp được xem cùng ảnh, class và quy tắc của task. Ground truth ba tier được phát **trong 60 phút cuối buổi lab** theo hướng dẫn lớp; đáp án checkpoint chỉ được dùng nếu người phụ trách cung cấp riêng.

| Task | Loại | Điểm tối đa | Điều cần chứng minh |
| --- | --- | ---: | --- |
| `easy_semantic` | Semantic | 20 | Phủ đúng vùng và lớp, nhất là road/sidewalk |
| `medium_instance` | Instance | 32 | Đủ vật, đúng class, từng vật một mask, biên theo phần nhìn thấy |
| `hard_panoptic` | Panoptic | 30 | Stuff và things cùng đúng; things tách instance, ít vùng bỏ trống/chồng lấn |
| Sáu checkpoint | Theo từng trạm | 6 × 3 = 18 | Xử lý lỗ, tách, nét mảnh, bó vỉa, che khuất, phủ vùng |
| **Tổng** | | **100** | |

Metric của starter gồm mIoU/coverage cho semantic, matched IoU và recall cho instance, PQ cho panoptic. **Chỉ có thể tính điểm so reference khi người chấm có ground truth phù hợp.** IoU giữa hai bản nhãn hoặc với gợi ý máy chỉ là độ giống nhau, không phải correctness. Điểm, cờ bất thường hoặc tốc độ không tự chứng minh người học gian lận; khi cần coach xem lại cách áp dụng quy tắc và bằng chứng trước/sau sửa.

## Điểm chính và bonus

Điểm chính tối đa 100. Bản Day03 hiện chưa giao nhiệm vụ bonus nên không tự cộng bonus hoặc xếp top 3. Nếu lớp bổ sung bonus, coach phải công bố nhiệm vụ, bằng chứng, tiêu chí và mức điểm riêng trước khi áp dụng; bonus tối đa 10, điểm ghi nhận cuối cùng tối đa 100. Scorecard ba tier chỉ phản hồi tối đa 82 điểm, không phải điểm cuối hoặc PASS.

## Cách đọc điểm kỹ thuật của starter

Khi reference đã được người chấm chuẩn bị và đối chiếu đúng ảnh/class, scorer gốc đổi metric thành điểm bằng `clamp((metric − floor)/(cap − floor), 0, 1) × trọng số`, làm tròn một chữ số. Đây là quy tắc chấm của starter, không phải lời hứa rằng tự kiểm ZIP sẽ cho điểm.

| Loại | Metric dùng để chấm | Floor | Cap nhận đủ điểm |
| --- | --- | ---: | ---: |
| Semantic | mIoU theo class; coverage là tín hiệu QC kèm theo | 0.40 | 0.85 |
| Instance | mean matched IoU × recall@0.5 | 0.40 | 0.85 |
| Panoptic | PQ trên stuff và từng thing | 0.20 | 0.65 |

Thiếu object làm recall giảm; một mask khít không bù được những vật bỏ sót. Với instance, object thừa làm giảm precision, nhưng precision không trực tiếp nằm trong công thức điểm hiện tại. Vì vậy điểm tự đánh giá cao không chứng minh bài không có object thừa; cần tự kiểm số vật trong CVAT. Mask thiếu/khác ảnh hoặc sai class cần kiểm lại trên CVAT trước khi bàn về điểm. Coach xem cả file xuất và report cho những ca quy tắc mơ hồ; không suy diễn hành vi của học viên từ một ngưỡng hay cờ kỹ thuật.

## Điều cần quan sát ở sáu checkpoint

| Trạm | Bằng chứng đúng | Lỗi dễ gặp cần sửa |
| --- | --- | --- |
| `cp1_holes` | Kính/khe nằm trong mask vật theo quy tắc task | Khoét lỗ tùy tiện khiến vật bị rỗng |
| `cp2_slice` | Hai xe sát nhau vẫn là hai instance | Một mask gộp hai xe |
| `cp5_occlusion` | Vật bị che vẫn được đếm là một instance | Tách thành hai object hoặc tự vẽ xuyên vùng bị che |
| `cp3_thin` | Nét mảnh có class đúng, xem ở zoom lớn | Bỏ cột/biển hoặc brush quá dày |
| `cp4_curb` | Ranh road–sidewalk theo chức năng/bó vỉa | Chọn theo màu nhựa đường |
| `cp6_coverage` | Vùng nhìn thấy thuộc lớp cần có được phủ | Khe trống lớn hoặc tô bừa vùng không chắc |

Mọi học viên có cùng bài, lớp và chuẩn bằng chứng. Hướng dẫn trực quan giúp người mới thao tác; người xong sớm có thể dùng reference để phân tích và sửa lỗi. Dùng công cụ hỗ trợ không thay thế việc tự kiểm và giải thích một quyết định gán nhãn.
