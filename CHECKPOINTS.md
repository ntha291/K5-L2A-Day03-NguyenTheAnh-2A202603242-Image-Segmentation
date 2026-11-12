# Checkpoints Day03

Mỗi trạm 1 ảnh, 3 điểm; đọc classes.json riêng trước khi tạo task.

## cp1_holes

- **Cần làm:** Giữ kính/chi tiết trong mask theo quy tắc task. Dùng ảnh trong `data/checkpoints/cp1_holes/images/`.
- **Sản phẩm:** `submissions/cp1_holes.zip`, export COCO 1.0.
- **Cần hiểu:** Phân biệt chi tiết bên trong vật và lỗ nền thật.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.

## cp2_slice

- **Cần làm:** Tách hai xe sát nhau thành hai instance. Dùng ảnh trong `data/checkpoints/cp2_slice/images/`.
- **Sản phẩm:** `submissions/cp2_slice.zip`, export COCO 1.0.
- **Cần hiểu:** Cùng class không đồng nghĩa cùng instance.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.

## cp3_thin

- **Cần làm:** Vẽ cột/biển mảnh ở zoom lớn. Dùng ảnh trong `data/checkpoints/cp3_thin/images/`.
- **Sản phẩm:** `submissions/cp3_thin.zip`, export Segmentation mask 1.1.
- **Cần hiểu:** Brush quá lớn làm tăng vùng nhãn sai.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.

## cp4_curb

- **Cần làm:** Vẽ ranh road–sidewalk theo bó vỉa và chức năng. Dùng ảnh trong `data/checkpoints/cp4_curb/images/`.
- **Sản phẩm:** `submissions/cp4_curb.zip`, export Segmentation mask 1.1.
- **Cần hiểu:** Không quyết định class chỉ theo màu.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.

## cp5_occlusion

- **Cần làm:** Giữ một instance cho các phần nhìn thấy của cùng vật. Dùng ảnh trong `data/checkpoints/cp5_occlusion/images/`.
- **Sản phẩm:** `submissions/cp5_occlusion.zip`, export COCO 1.0.
- **Cần hiểu:** Không vẽ phần bị che; không tách ID vì bị che.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.

## cp6_coverage

- **Cần làm:** Phủ vùng nhìn thấy thuộc schema. Dùng ảnh trong `data/checkpoints/cp6_coverage/images/`.
- **Sản phẩm:** `submissions/cp6_coverage.zip`, export Segmentation mask 1.1.
- **Cần hiểu:** Coverage cần đối chiếu class, không tô ép vùng chưa chắc.
- **Tự kiểm:** đúng ảnh/class của trạm, vùng nhìn thấy, số object, biên; Save, export và mở ZIP kiểm có dữ liệu. Nếu có lỗi thật, ghi vị trí/quy tắc/sửa trong report.
- **Chấm:** tối đa 3 điểm theo metric loại task và [RUBRIC](RUBRIC.md); chưa có reference không tự ghi điểm.
