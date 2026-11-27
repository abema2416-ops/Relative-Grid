// Lean compiler output
// Module: Setka.Heights
// Imports: public import Init public meta import Init public import Setka.Basic
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lean_nat_pow(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lean_nat_mul(lean_object*, lean_object*);
lean_object* lean_nat_shiftr(lean_object*, lean_object*);
lean_object* lean_nat_mod(lean_object*, lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_prodMask(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_prodMask___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_ladder(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_ladder___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___redArg___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_prodMask_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_prodMask_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_disappeared(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_disappeared___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_preimages(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_preimages___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_disappeared_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_disappeared_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_prodMask(lean_object* v_x_1_, lean_object* v_x_2_){
_start:
{
if (lean_obj_tag(v_x_1_) == 0)
{
lean_object* v___x_3_; 
v___x_3_ = lean_unsigned_to_nat(1u);
return v___x_3_;
}
else
{
lean_object* v_head_4_; lean_object* v_tail_5_; lean_object* v___y_7_; lean_object* v___x_12_; lean_object* v___x_13_; lean_object* v___x_14_; uint8_t v___x_15_; 
v_head_4_ = lean_ctor_get(v_x_1_, 0);
v_tail_5_ = lean_ctor_get(v_x_1_, 1);
v___x_12_ = lean_unsigned_to_nat(2u);
v___x_13_ = lean_nat_mod(v_x_2_, v___x_12_);
v___x_14_ = lean_unsigned_to_nat(1u);
v___x_15_ = lean_nat_dec_eq(v___x_13_, v___x_14_);
lean_dec(v___x_13_);
if (v___x_15_ == 0)
{
v___y_7_ = v___x_14_;
goto v___jp_6_;
}
else
{
v___y_7_ = v_head_4_;
goto v___jp_6_;
}
v___jp_6_:
{
lean_object* v___x_8_; lean_object* v___x_9_; lean_object* v___x_10_; lean_object* v___x_11_; 
v___x_8_ = lean_unsigned_to_nat(1u);
v___x_9_ = lean_nat_shiftr(v_x_2_, v___x_8_);
v___x_10_ = lp_setka_Setka_prodMask(v_tail_5_, v___x_9_);
lean_dec(v___x_9_);
v___x_11_ = lean_nat_mul(v___y_7_, v___x_10_);
lean_dec(v___x_10_);
return v___x_11_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_prodMask___boxed(lean_object* v_x_16_, lean_object* v_x_17_){
_start:
{
lean_object* v_res_18_; 
v_res_18_ = lp_setka_Setka_prodMask(v_x_16_, v_x_17_);
lean_dec(v_x_17_);
lean_dec(v_x_16_);
return v_res_18_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_ladder(lean_object* v_b_19_, lean_object* v_x_20_){
_start:
{
lean_object* v_zero_21_; uint8_t v_isZero_22_; 
v_zero_21_ = lean_unsigned_to_nat(0u);
v_isZero_22_ = lean_nat_dec_eq(v_x_20_, v_zero_21_);
if (v_isZero_22_ == 1)
{
lean_object* v___x_23_; 
lean_dec(v_b_19_);
v___x_23_ = lean_box(0);
return v___x_23_;
}
else
{
lean_object* v_one_24_; lean_object* v_n_25_; lean_object* v___x_26_; lean_object* v___x_27_; lean_object* v___x_28_; 
v_one_24_ = lean_unsigned_to_nat(1u);
v_n_25_ = lean_nat_sub(v_x_20_, v_one_24_);
v___x_26_ = lean_nat_mul(v_b_19_, v_b_19_);
v___x_27_ = lp_setka_Setka_ladder(v___x_26_, v_n_25_);
lean_dec(v_n_25_);
v___x_28_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_28_, 0, v_b_19_);
lean_ctor_set(v___x_28_, 1, v___x_27_);
return v___x_28_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_ladder___boxed(lean_object* v_b_29_, lean_object* v_x_30_){
_start:
{
lean_object* v_res_31_; 
v_res_31_ = lp_setka_Setka_ladder(v_b_29_, v_x_30_);
lean_dec(v_x_30_);
return v_res_31_;
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___redArg(lean_object* v_x_32_, lean_object* v_h__1_33_, lean_object* v_h__2_34_){
_start:
{
lean_object* v_zero_35_; uint8_t v_isZero_36_; 
v_zero_35_ = lean_unsigned_to_nat(0u);
v_isZero_36_ = lean_nat_dec_eq(v_x_32_, v_zero_35_);
if (v_isZero_36_ == 1)
{
lean_object* v___x_37_; lean_object* v___x_38_; 
lean_dec(v_h__2_34_);
v___x_37_ = lean_box(0);
v___x_38_ = lean_apply_1(v_h__1_33_, v___x_37_);
return v___x_38_;
}
else
{
lean_object* v_one_39_; lean_object* v_n_40_; lean_object* v___x_41_; 
lean_dec(v_h__1_33_);
v_one_39_ = lean_unsigned_to_nat(1u);
v_n_40_ = lean_nat_sub(v_x_32_, v_one_39_);
v___x_41_ = lean_apply_1(v_h__2_34_, v_n_40_);
return v___x_41_;
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___redArg___boxed(lean_object* v_x_42_, lean_object* v_h__1_43_, lean_object* v_h__2_44_){
_start:
{
lean_object* v_res_45_; 
v_res_45_ = lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___redArg(v_x_42_, v_h__1_43_, v_h__2_44_);
lean_dec(v_x_42_);
return v_res_45_;
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter(lean_object* v_motive_46_, lean_object* v_x_47_, lean_object* v_h__1_48_, lean_object* v_h__2_49_){
_start:
{
lean_object* v_zero_50_; uint8_t v_isZero_51_; 
v_zero_50_ = lean_unsigned_to_nat(0u);
v_isZero_51_ = lean_nat_dec_eq(v_x_47_, v_zero_50_);
if (v_isZero_51_ == 1)
{
lean_object* v___x_52_; lean_object* v___x_53_; 
lean_dec(v_h__2_49_);
v___x_52_ = lean_box(0);
v___x_53_ = lean_apply_1(v_h__1_48_, v___x_52_);
return v___x_53_;
}
else
{
lean_object* v_one_54_; lean_object* v_n_55_; lean_object* v___x_56_; 
lean_dec(v_h__1_48_);
v_one_54_ = lean_unsigned_to_nat(1u);
v_n_55_ = lean_nat_sub(v_x_47_, v_one_54_);
v___x_56_ = lean_apply_1(v_h__2_49_, v_n_55_);
return v___x_56_;
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter___boxed(lean_object* v_motive_57_, lean_object* v_x_58_, lean_object* v_h__1_59_, lean_object* v_h__2_60_){
_start:
{
lean_object* v_res_61_; 
v_res_61_ = lp_setka___private_Setka_Heights_0__Setka_ladder_match__1_splitter(v_motive_57_, v_x_58_, v_h__1_59_, v_h__2_60_);
lean_dec(v_x_58_);
return v_res_61_;
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_prodMask_match__1_splitter___redArg(lean_object* v_x_62_, lean_object* v_x_63_, lean_object* v_h__1_64_, lean_object* v_h__2_65_){
_start:
{
if (lean_obj_tag(v_x_62_) == 0)
{
lean_object* v___x_66_; 
lean_dec(v_h__2_65_);
v___x_66_ = lean_apply_1(v_h__1_64_, v_x_63_);
return v___x_66_;
}
else
{
lean_object* v_head_67_; lean_object* v_tail_68_; lean_object* v___x_69_; 
lean_dec(v_h__1_64_);
v_head_67_ = lean_ctor_get(v_x_62_, 0);
lean_inc(v_head_67_);
v_tail_68_ = lean_ctor_get(v_x_62_, 1);
lean_inc(v_tail_68_);
lean_dec_ref_known(v_x_62_, 2);
v___x_69_ = lean_apply_3(v_h__2_65_, v_head_67_, v_tail_68_, v_x_63_);
return v___x_69_;
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_prodMask_match__1_splitter(lean_object* v_motive_70_, lean_object* v_x_71_, lean_object* v_x_72_, lean_object* v_h__1_73_, lean_object* v_h__2_74_){
_start:
{
if (lean_obj_tag(v_x_71_) == 0)
{
lean_object* v___x_75_; 
lean_dec(v_h__2_74_);
v___x_75_ = lean_apply_1(v_h__1_73_, v_x_72_);
return v___x_75_;
}
else
{
lean_object* v_head_76_; lean_object* v_tail_77_; lean_object* v___x_78_; 
lean_dec(v_h__1_73_);
v_head_76_ = lean_ctor_get(v_x_71_, 0);
lean_inc(v_head_76_);
v_tail_77_ = lean_ctor_get(v_x_71_, 1);
lean_inc(v_tail_77_);
lean_dec_ref_known(v_x_71_, 2);
v___x_78_ = lean_apply_3(v_h__2_74_, v_head_76_, v_tail_77_, v_x_72_);
return v___x_78_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_disappeared(lean_object* v_x_79_){
_start:
{
if (lean_obj_tag(v_x_79_) == 0)
{
lean_object* v___x_80_; 
v___x_80_ = lean_unsigned_to_nat(0u);
return v___x_80_;
}
else
{
lean_object* v_head_81_; lean_object* v_tail_82_; lean_object* v___x_83_; lean_object* v___x_84_; lean_object* v___x_85_; lean_object* v___x_86_; 
v_head_81_ = lean_ctor_get(v_x_79_, 0);
v_tail_82_ = lean_ctor_get(v_x_79_, 1);
v___x_83_ = lean_unsigned_to_nat(1u);
v___x_84_ = lean_nat_sub(v_head_81_, v___x_83_);
v___x_85_ = lp_setka_Setka_disappeared(v_tail_82_);
v___x_86_ = lean_nat_add(v___x_84_, v___x_85_);
lean_dec(v___x_85_);
lean_dec(v___x_84_);
return v___x_86_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_disappeared___boxed(lean_object* v_x_87_){
_start:
{
lean_object* v_res_88_; 
v_res_88_ = lp_setka_Setka_disappeared(v_x_87_);
lean_dec(v_x_87_);
return v_res_88_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_preimages(lean_object* v_x_89_){
_start:
{
if (lean_obj_tag(v_x_89_) == 0)
{
lean_object* v___x_90_; 
v___x_90_ = lean_unsigned_to_nat(1u);
return v___x_90_;
}
else
{
lean_object* v_head_91_; lean_object* v_tail_92_; lean_object* v___x_93_; lean_object* v___x_94_; lean_object* v___x_95_; lean_object* v___x_96_; lean_object* v___x_97_; lean_object* v___x_98_; 
v_head_91_ = lean_ctor_get(v_x_89_, 0);
v_tail_92_ = lean_ctor_get(v_x_89_, 1);
v___x_93_ = lean_unsigned_to_nat(2u);
v___x_94_ = lean_nat_pow(v___x_93_, v_head_91_);
v___x_95_ = lean_unsigned_to_nat(1u);
v___x_96_ = lean_nat_sub(v___x_94_, v___x_95_);
lean_dec(v___x_94_);
v___x_97_ = lp_setka_Setka_preimages(v_tail_92_);
v___x_98_ = lean_nat_mul(v___x_96_, v___x_97_);
lean_dec(v___x_97_);
lean_dec(v___x_96_);
return v___x_98_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_preimages___boxed(lean_object* v_x_99_){
_start:
{
lean_object* v_res_100_; 
v_res_100_ = lp_setka_Setka_preimages(v_x_99_);
lean_dec(v_x_99_);
return v_res_100_;
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_disappeared_match__1_splitter___redArg(lean_object* v_x_101_, lean_object* v_h__1_102_, lean_object* v_h__2_103_){
_start:
{
if (lean_obj_tag(v_x_101_) == 0)
{
lean_object* v___x_104_; lean_object* v___x_105_; 
lean_dec(v_h__2_103_);
v___x_104_ = lean_box(0);
v___x_105_ = lean_apply_1(v_h__1_102_, v___x_104_);
return v___x_105_;
}
else
{
lean_object* v_head_106_; lean_object* v_tail_107_; lean_object* v___x_108_; 
lean_dec(v_h__1_102_);
v_head_106_ = lean_ctor_get(v_x_101_, 0);
lean_inc(v_head_106_);
v_tail_107_ = lean_ctor_get(v_x_101_, 1);
lean_inc(v_tail_107_);
lean_dec_ref_known(v_x_101_, 2);
v___x_108_ = lean_apply_2(v_h__2_103_, v_head_106_, v_tail_107_);
return v___x_108_;
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Heights_0__Setka_disappeared_match__1_splitter(lean_object* v_motive_109_, lean_object* v_x_110_, lean_object* v_h__1_111_, lean_object* v_h__2_112_){
_start:
{
if (lean_obj_tag(v_x_110_) == 0)
{
lean_object* v___x_113_; lean_object* v___x_114_; 
lean_dec(v_h__2_112_);
v___x_113_ = lean_box(0);
v___x_114_ = lean_apply_1(v_h__1_111_, v___x_113_);
return v___x_114_;
}
else
{
lean_object* v_head_115_; lean_object* v_tail_116_; lean_object* v___x_117_; 
lean_dec(v_h__1_111_);
v_head_115_ = lean_ctor_get(v_x_110_, 0);
lean_inc(v_head_115_);
v_tail_116_ = lean_ctor_get(v_x_110_, 1);
lean_inc(v_tail_116_);
lean_dec_ref_known(v_x_110_, 2);
v___x_117_ = lean_apply_2(v_h__2_112_, v_head_115_, v_tail_116_);
return v___x_117_;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_setka_Setka_Basic(uint8_t builtin);
void lean_initialize_runtime_module();
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_setka_Setka_Heights(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
lean_initialize_runtime_module();
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_setka_Setka_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
