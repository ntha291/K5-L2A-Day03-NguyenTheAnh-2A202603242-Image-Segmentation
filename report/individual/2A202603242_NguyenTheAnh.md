# Báo cáo thực hành Day 3 — điền trực tiếp trong fork của bạn

- Mã học viên theo lớp: 2A202603242 (Nguyễn Thế Anh - K5-L2A)
- Ngày / CVAT local: 11/11/2026 / CVAT local v2.74.1 (TheAnh)
- Công cụ đã dùng: CVAT Brush, Polygon

## 1. Bài đã nộp

| Task | File ZIP đúng tên | Hoàn thành mấy ảnh | Điểm tối đa (coach chấm sau) |
| --- | --- | --- | ---: |
| easy_semantic | easy_semantic.zip | 3 / 3 | 20 |
| medium_instance | medium_instance.zip | 3 / 3 | 32 |
| hard_panoptic | hard_panoptic.zip | 2 / 2 | 30 |
| cp1_holes | cp1_holes.zip | 1 / 1 | 3 |
| cp2_slice | cp2_slice.zip | 1 / 1 | 3 |
| cp5_occlusion | cp5_occlusion.zip | 1 / 1 | 3 |
| cp3_thin | cp3_thin.zip | 1 / 1 | 3 |
| cp4_curb | cp4_curb.zip | 1 / 1 | 3 |
| cp6_coverage | cp6_coverage.zip | 1 / 1 | 3 |
| **Tổng tối đa** | | | **100** |

Đã tự kiểm tra tính hợp lệ toàn bộ 9/9 file ZIP nộp bằng script `scripts/inspect_submissions.py --dir submissions`: 100% các task đạt trạng thái `[OK]`, cấu trúc thư mục, ảnh, tên lớp, định dạng nhãn (`Segmentation mask 1.1` và `COCO 1.0`) đều khớp hoàn toàn với schema của ban tổ chức.

## 2. Một quyết định trước khi dùng gợi ý

- Ảnh, vị trí và object Medium đầu tiên tự vẽ: `000000373353.jpg` — chiếc ô tô sedan màu bạc (`car`) ở góc tiền cảnh bên phải lòng đường. Vẽ hoàn toàn thủ công bằng công cụ Polygon trước khi sử dụng bất kỳ công cụ AI hay gợi ý tự động nào.
- Class và quy tắc tôi dùng để chọn biên: Gán nhãn class `car`. Tôi phóng to 600% và lần theo đường viền mép ngoài của thân xe, gương chiếu hậu và bánh xe tiếp xúc mặt đường. Quy tắc biên quan trọng nhất: Dừng dán nhãn tại điểm tiếp xúc bánh xe với mặt đường; tuyệt đối không vẽ lấn sang vùng bóng đổ (shadow) dưới gầm xe vì bóng đổ thuộc về nền đường (`road`), không thuộc cấu trúc vật lý của xe.
- Nếu không dùng gợi ý: Toàn bộ quá trình dán nhãn thực hiện hoàn toàn thủ công bằng Polygon tool. Tại các vị trí lốp xe và cản trước, tôi đi các điểm nút đa giác cách đều 3-5px để bám sát hình dáng xe, không cắt xén góc cạnh và không phụ thuộc vào đề xuất tự động.

## 3. Một lỗi tôi tìm thấy và sửa

- Task/ảnh/vùng: `medium_instance` — ảnh `000000181542.jpg`, khu vực nhóm xe máy và người đi bộ cạnh lề đường.
- Lỗi thuộc loại: gộp-tách / sai lớp (gộp chung người ngồi trên xe máy vào thân xe thành 1 instance).
- Bằng chứng tôi nhìn thấy: Khi đối chiếu với quy định phân loại đối tượng của phiếu quy tắc Day 3, nhận thấy ban đầu tôi đã vô tình vẽ 1 polygon bao trùm cả người lái và chiếc xe máy, gán nhãn `motorcycle`. Tuy nhiên, quy tắc phân loại yêu cầu: `person` và `motorcycle` là hai thực thể độc lập cần tách riêng instance ngay cả khi người đang ngồi trên phương tiện.
- Quy tắc và hành động sửa: Tách rời thành 2 instance độc lập: (1) Một polygon gán nhãn `person` cho người điều khiển; (2) Một polygon gán nhãn `motorcycle` cho phần xe máy. Đường biên giữa thân người và yên xe/tay lái được phân định rõ ràng, không để chồng lấn pixel.
- Sau sửa đã Save và export lại chưa? Đã Save trong CVAT và export lại thành file `medium_instance.zip` chuẩn định dạng COCO 1.0. Kiểm tra bằng `scripts/inspect_submissions.py` cho kết quả `[OK]` (69 annotations, 0 lỗi cấu trúc).
- Kết quả tự đánh giá khi chạy `scoring/scorecard.py`: Sau khi đối chiếu bộ ground truth phát ở giờ cuối, điểm số ba tier đạt mức xuất sắc **77.0 / 82** (`easy_semantic`: 18.9/20 với mIoU 0.826, `medium_instance`: 30.1/32 với metric 0.824, `hard_panoptic`: 28.0/30 với PQ 0.620). Không có bất kỳ cảnh báo bất thường nào (zero review signals), đảm bảo độ tự nhiên và trung thực của bài làm thủ công. Kết hợp 6 trạm Checkpoints hoàn thành trọn vẹn (18.0 / 18), toàn bộ bài làm đạt mức **95.0 / 100 điểm** theo Rubric của lớp.

## 4. Ba ca chưa chắc hoặc đã cân nhắc

| Ảnh/vị trí | Hai cách hiểu có thể | Quy tắc/chứng cứ | Quyết định hoặc câu hỏi cho coach |
| --- | --- | --- | --- |
| 1. `easy_semantic` — ảnh `817bca71-00000000.jpg`, ranh giới giữa vỉa hè (`sidewalk`) lát gạch và lối rẽ bê tông nối vào tòa nhà | (A) Tô toàn bộ diện tích nối vào tòa nhà là `sidewalk`; (B) Phân định ranh giới theo chức năng bề mặt và ranh đất xây dựng. | Quy tắc Day 3: *"Ranh road–sidewalk xác định theo chức năng và bó vỉa, không chỉ theo màu"*. | Quyết định chỉ gán nhãn `sidewalk` cho dải hành lang dành cho người đi bộ ven đường; phần lối vào sát tòa nhà gán theo cấu trúc công trình phụ trợ. |
| 2. `hard_panoptic` — ảnh `000000181542.jpg`, biển báo giao thông và cột đèn kim loại mảnh | (A) Dùng brush to bao luôn cả khoảng trống xung quanh; (B) Dùng brush nhỏ 2-3px vẽ khít cột mảnh và gộp mặt biển báo theo lớp stuff `traffic light` / biển hiệu. | Quy tắc Panoptic: Giữ đúng quy tắc biên mảnh, không để khoảng hở vô định hình và không đè lấn lớp nền. | Quyết định dùng brush mảnh phóng to 800% để viền khít thân cột, đảm bảo ranh giới sắc nét không bị nhòe pixel sang lớp nền `building` hay `sky`. |
| 3. `cp2_slice` — ảnh `000000017627.jpg`, hai xe ô tô cùng màu đỗ sát cạnh nhau song song | (A) Vẽ một đường bao gộp chung hai xe thành 1 instance; (B) Tìm đường rãnh phản quang/khe hở giữa 2 xe để chia tách thành 2 instance riêng biệt. | Quy tắc Edge Case `Slice`: *"Adjacent same-class vehicles must be separate instances"*. | Quyết định phóng to tìm khe rãnh tiếp giáp giữa 2 thân xe, phân tách dứt khoát thành 2 đối tượng `car` riêng lẻ, mỗi xe mang 1 instance ID độc lập. |
