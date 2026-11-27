// Lean compiler output
// Module: Setka.Core
// Imports: public import Init public meta import Init public import Setka.Basic public import Setka.Stretch
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
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_int_mul(lean_object*, lean_object*);
lean_object* lean_int_sub(lean_object*, lean_object*);
lean_object* lean_nat_to_int(lean_object*);
lean_object* lean_int_ediv(lean_object*, lean_object*);
lean_object* lean_int_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___redArg___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___redArg___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___redArg(lean_object* v_x_1_, lean_object* v_i_2_, lean_object* v_v_3_, lean_object* v_k_4_){
_start:
{
uint8_t v___x_5_; 
v___x_5_ = lean_nat_dec_eq(v_k_4_, v_i_2_);
if (v___x_5_ == 0)
{
lean_object* v___x_6_; 
v___x_6_ = lean_apply_1(v_x_1_, v_k_4_);
return v___x_6_;
}
else
{
lean_dec(v_k_4_);
lean_dec_ref(v_x_1_);
lean_inc(v_v_3_);
return v_v_3_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___redArg___boxed(lean_object* v_x_7_, lean_object* v_i_8_, lean_object* v_v_9_, lean_object* v_k_10_){
_start:
{
lean_object* v_res_11_; 
v_res_11_ = lp_setka_Setka_Core_upd___redArg(v_x_7_, v_i_8_, v_v_9_, v_k_10_);
lean_dec(v_v_9_);
lean_dec(v_i_8_);
return v_res_11_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd(lean_object* v_n_12_, lean_object* v_x_13_, lean_object* v_i_14_, lean_object* v_v_15_, lean_object* v_k_16_){
_start:
{
lean_object* v___x_17_; 
v___x_17_ = lp_setka_Setka_Core_upd___redArg(v_x_13_, v_i_14_, v_v_15_, v_k_16_);
return v___x_17_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_upd___boxed(lean_object* v_n_18_, lean_object* v_x_19_, lean_object* v_i_20_, lean_object* v_v_21_, lean_object* v_k_22_){
_start:
{
lean_object* v_res_23_; 
v_res_23_ = lp_setka_Setka_Core_upd(v_n_18_, v_x_19_, v_i_20_, v_v_21_, v_k_22_);
lean_dec(v_v_21_);
lean_dec(v_i_20_);
lean_dec(v_n_18_);
return v_res_23_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___redArg(lean_object* v_i_24_, lean_object* v_s_25_, lean_object* v_f_26_, lean_object* v_a_27_, lean_object* v_c_28_, lean_object* v_a_29_){
_start:
{
lean_object* v___x_30_; lean_object* v___x_31_; lean_object* v___x_32_; lean_object* v___x_33_; lean_object* v___x_34_; lean_object* v___x_35_; lean_object* v___x_36_; lean_object* v___x_37_; 
lean_inc_ref(v_c_28_);
lean_inc(v_i_24_);
v___x_30_ = lean_apply_1(v_c_28_, v_i_24_);
v___x_31_ = lean_int_mul(v_s_25_, v___x_30_);
lean_dec(v___x_30_);
v___x_32_ = lean_int_sub(v___x_31_, v_a_27_);
lean_dec(v___x_31_);
v___x_33_ = lean_nat_to_int(v_f_26_);
v___x_34_ = lean_int_ediv(v___x_32_, v___x_33_);
lean_dec(v___x_33_);
lean_dec(v___x_32_);
v___x_35_ = lean_int_add(v_a_27_, v___x_34_);
lean_dec(v___x_34_);
v___x_36_ = lean_int_mul(v_s_25_, v___x_35_);
lean_dec(v___x_35_);
v___x_37_ = lp_setka_Setka_Core_upd___redArg(v_c_28_, v_i_24_, v___x_36_, v_a_29_);
lean_dec(v___x_36_);
lean_dec(v_i_24_);
return v___x_37_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___redArg___boxed(lean_object* v_i_38_, lean_object* v_s_39_, lean_object* v_f_40_, lean_object* v_a_41_, lean_object* v_c_42_, lean_object* v_a_43_){
_start:
{
lean_object* v_res_44_; 
v_res_44_ = lp_setka_Setka_Core_shrinkCell___redArg(v_i_38_, v_s_39_, v_f_40_, v_a_41_, v_c_42_, v_a_43_);
lean_dec(v_a_41_);
lean_dec(v_s_39_);
return v_res_44_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell(lean_object* v_n_45_, lean_object* v_i_46_, lean_object* v_s_47_, lean_object* v_f_48_, lean_object* v_a_49_, lean_object* v_c_50_, lean_object* v_a_51_){
_start:
{
lean_object* v___x_52_; 
v___x_52_ = lp_setka_Setka_Core_shrinkCell___redArg(v_i_46_, v_s_47_, v_f_48_, v_a_49_, v_c_50_, v_a_51_);
return v___x_52_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Core_shrinkCell___boxed(lean_object* v_n_53_, lean_object* v_i_54_, lean_object* v_s_55_, lean_object* v_f_56_, lean_object* v_a_57_, lean_object* v_c_58_, lean_object* v_a_59_){
_start:
{
lean_object* v_res_60_; 
v_res_60_ = lp_setka_Setka_Core_shrinkCell(v_n_53_, v_i_54_, v_s_55_, v_f_56_, v_a_57_, v_c_58_, v_a_59_);
lean_dec(v_a_57_);
lean_dec(v_s_55_);
lean_dec(v_n_53_);
return v_res_60_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_setka_Setka_Basic(uint8_t builtin);
lean_object* initialize_setka_Setka_Stretch(uint8_t builtin);
void lean_initialize_runtime_module();
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_setka_Setka_Core(uint8_t builtin) {
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
res = initialize_setka_Setka_Stretch(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
