// Lean compiler output
// Module: Setka.Glue
// Imports: public import Init public meta import Init
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
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* lean_nat_mod(lean_object*, lean_object*);
lean_object* l_List_finRange(lean_object*);
lean_object* lean_int_add(lean_object*, lean_object*);
lean_object* l_List_reverse___redArg(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* lean_int_sub(lean_object*, lean_object*);
lean_object* lean_obj_tag_nat(lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
uint8_t l_Nat_testBit(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_nxt(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_nxt___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_prv(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_prv___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_setka_List_all___at___00Setka_valid_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_List_all___at___00Setka_valid_spec__0___boxed(lean_object*, lean_object*, lean_object*);
static lean_once_cell_t lp_setka_Setka_valid___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_setka_Setka_valid___closed__0;
LEAN_EXPORT uint8_t lp_setka_Setka_valid(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_valid___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_setka_Setka_adj(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_adj___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_setka_Setka_reach(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_setka_List_any___at___00Setka_reach_spec__0(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_List_any___at___00Setka_reach_spec__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_reach___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_setka_List_all___at___00Setka_comps_spec__0(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_List_all___at___00Setka_comps_spec__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_List_filterTR_loop___at___00Setka_comps_spec__1(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_comps(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_List_filterTR_loop___at___00Setka_kk_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_kk(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_ss(lean_object*);
LEAN_EXPORT uint8_t lp_setka_Setka_bits(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_bits___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_dd(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_dd___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorIdx___impl(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorIdx___impl___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_stretch_elim___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_stretch_elim(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_glue_elim___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_Step_glue_elim(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_run(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_run___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_glues(lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_glues___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_run_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_run_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_glues_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_glues_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_setka_Setka_nxt(lean_object* v_i_1_){
_start:
{
lean_object* v___x_2_; lean_object* v___x_3_; lean_object* v___x_4_; lean_object* v___x_5_; 
v___x_2_ = lean_unsigned_to_nat(4u);
v___x_3_ = lean_unsigned_to_nat(1u);
v___x_4_ = lean_nat_add(v_i_1_, v___x_3_);
v___x_5_ = lean_nat_mod(v___x_4_, v___x_2_);
lean_dec(v___x_4_);
return v___x_5_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_nxt___boxed(lean_object* v_i_6_){
_start:
{
lean_object* v_res_7_; 
v_res_7_ = lp_setka_Setka_nxt(v_i_6_);
lean_dec(v_i_6_);
return v_res_7_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_prv(lean_object* v_i_8_){
_start:
{
lean_object* v___x_9_; lean_object* v___x_10_; lean_object* v___x_11_; lean_object* v___x_12_; 
v___x_9_ = lean_unsigned_to_nat(4u);
v___x_10_ = lean_unsigned_to_nat(3u);
v___x_11_ = lean_nat_add(v_i_8_, v___x_10_);
v___x_12_ = lean_nat_mod(v___x_11_, v___x_9_);
lean_dec(v___x_11_);
return v___x_12_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_prv___boxed(lean_object* v_i_13_){
_start:
{
lean_object* v_res_14_; 
v_res_14_ = lp_setka_Setka_prv(v_i_13_);
lean_dec(v_i_13_);
return v_res_14_;
}
}
LEAN_EXPORT uint8_t lp_setka_List_all___at___00Setka_valid_spec__0(lean_object* v_glue_15_, lean_object* v_pres_16_, lean_object* v_x_17_){
_start:
{
if (lean_obj_tag(v_x_17_) == 0)
{
uint8_t v___x_18_; 
lean_dec_ref(v_pres_16_);
lean_dec_ref(v_glue_15_);
v___x_18_ = 1;
return v___x_18_;
}
else
{
lean_object* v_head_19_; lean_object* v_tail_20_; lean_object* v___x_21_; uint8_t v___x_22_; 
v_head_19_ = lean_ctor_get(v_x_17_, 0);
lean_inc_n(v_head_19_, 2);
v_tail_20_ = lean_ctor_get(v_x_17_, 1);
lean_inc(v_tail_20_);
lean_dec_ref_known(v_x_17_, 2);
lean_inc_ref(v_glue_15_);
v___x_21_ = lean_apply_1(v_glue_15_, v_head_19_);
v___x_22_ = lean_unbox(v___x_21_);
if (v___x_22_ == 0)
{
lean_dec(v_head_19_);
v_x_17_ = v_tail_20_;
goto _start;
}
else
{
lean_object* v___x_24_; uint8_t v___x_25_; 
lean_inc_ref(v_pres_16_);
lean_inc(v_head_19_);
v___x_24_ = lean_apply_1(v_pres_16_, v_head_19_);
v___x_25_ = lean_unbox(v___x_24_);
if (v___x_25_ == 0)
{
uint8_t v___x_26_; 
lean_dec(v_tail_20_);
lean_dec(v_head_19_);
lean_dec_ref(v_pres_16_);
lean_dec_ref(v_glue_15_);
v___x_26_ = lean_unbox(v___x_24_);
return v___x_26_;
}
else
{
lean_object* v___x_27_; lean_object* v___x_28_; uint8_t v___x_29_; 
v___x_27_ = lp_setka_Setka_nxt(v_head_19_);
lean_dec(v_head_19_);
lean_inc_ref(v_pres_16_);
v___x_28_ = lean_apply_1(v_pres_16_, v___x_27_);
v___x_29_ = lean_unbox(v___x_28_);
if (v___x_29_ == 0)
{
uint8_t v___x_30_; 
lean_dec(v_tail_20_);
lean_dec_ref(v_pres_16_);
lean_dec_ref(v_glue_15_);
v___x_30_ = lean_unbox(v___x_28_);
return v___x_30_;
}
else
{
v_x_17_ = v_tail_20_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_List_all___at___00Setka_valid_spec__0___boxed(lean_object* v_glue_32_, lean_object* v_pres_33_, lean_object* v_x_34_){
_start:
{
uint8_t v_res_35_; lean_object* v_r_36_; 
v_res_35_ = lp_setka_List_all___at___00Setka_valid_spec__0(v_glue_32_, v_pres_33_, v_x_34_);
v_r_36_ = lean_box(v_res_35_);
return v_r_36_;
}
}
static lean_object* _init_lp_setka_Setka_valid___closed__0(void){
_start:
{
lean_object* v___x_37_; lean_object* v___x_38_; 
v___x_37_ = lean_unsigned_to_nat(4u);
v___x_38_ = l_List_finRange(v___x_37_);
return v___x_38_;
}
}
LEAN_EXPORT uint8_t lp_setka_Setka_valid(lean_object* v_pres_39_, lean_object* v_glue_40_){
_start:
{
lean_object* v___x_41_; uint8_t v___x_42_; 
v___x_41_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_42_ = lp_setka_List_all___at___00Setka_valid_spec__0(v_glue_40_, v_pres_39_, v___x_41_);
return v___x_42_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_valid___boxed(lean_object* v_pres_43_, lean_object* v_glue_44_){
_start:
{
uint8_t v_res_45_; lean_object* v_r_46_; 
v_res_45_ = lp_setka_Setka_valid(v_pres_43_, v_glue_44_);
v_r_46_ = lean_box(v_res_45_);
return v_r_46_;
}
}
LEAN_EXPORT uint8_t lp_setka_Setka_adj(lean_object* v_glue_47_, lean_object* v_i_48_, lean_object* v_j_49_){
_start:
{
lean_object* v___x_56_; uint8_t v___x_57_; 
lean_inc_ref(v_glue_47_);
lean_inc(v_i_48_);
v___x_56_ = lean_apply_1(v_glue_47_, v_i_48_);
v___x_57_ = lean_unbox(v___x_56_);
if (v___x_57_ == 0)
{
goto v___jp_50_;
}
else
{
lean_object* v___x_58_; uint8_t v___x_59_; 
v___x_58_ = lp_setka_Setka_nxt(v_i_48_);
v___x_59_ = lean_nat_dec_eq(v_j_49_, v___x_58_);
lean_dec(v___x_58_);
if (v___x_59_ == 0)
{
goto v___jp_50_;
}
else
{
lean_dec(v_j_49_);
lean_dec(v_i_48_);
lean_dec_ref(v_glue_47_);
return v___x_59_;
}
}
v___jp_50_:
{
lean_object* v___x_51_; uint8_t v___x_52_; 
lean_inc(v_j_49_);
v___x_51_ = lean_apply_1(v_glue_47_, v_j_49_);
v___x_52_ = lean_unbox(v___x_51_);
if (v___x_52_ == 0)
{
uint8_t v___x_53_; 
lean_dec(v_j_49_);
lean_dec(v_i_48_);
v___x_53_ = lean_unbox(v___x_51_);
return v___x_53_;
}
else
{
lean_object* v___x_54_; uint8_t v___x_55_; 
v___x_54_ = lp_setka_Setka_nxt(v_j_49_);
lean_dec(v_j_49_);
v___x_55_ = lean_nat_dec_eq(v_i_48_, v___x_54_);
lean_dec(v___x_54_);
lean_dec(v_i_48_);
return v___x_55_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_adj___boxed(lean_object* v_glue_60_, lean_object* v_i_61_, lean_object* v_j_62_){
_start:
{
uint8_t v_res_63_; lean_object* v_r_64_; 
v_res_63_ = lp_setka_Setka_adj(v_glue_60_, v_i_61_, v_j_62_);
v_r_64_ = lean_box(v_res_63_);
return v_r_64_;
}
}
LEAN_EXPORT uint8_t lp_setka_Setka_reach(lean_object* v_glue_65_, lean_object* v_x_66_, lean_object* v_x_67_, lean_object* v_x_68_){
_start:
{
lean_object* v_zero_69_; uint8_t v_isZero_70_; 
v_zero_69_ = lean_unsigned_to_nat(0u);
v_isZero_70_ = lean_nat_dec_eq(v_x_66_, v_zero_69_);
if (v_isZero_70_ == 1)
{
uint8_t v___x_71_; 
lean_dec_ref(v_glue_65_);
v___x_71_ = lean_nat_dec_eq(v_x_67_, v_x_68_);
lean_dec(v_x_68_);
return v___x_71_;
}
else
{
lean_object* v_one_72_; lean_object* v_n_73_; uint8_t v___x_74_; 
v_one_72_ = lean_unsigned_to_nat(1u);
v_n_73_ = lean_nat_sub(v_x_66_, v_one_72_);
lean_inc(v_x_68_);
lean_inc_ref(v_glue_65_);
v___x_74_ = lp_setka_Setka_reach(v_glue_65_, v_n_73_, v_x_67_, v_x_68_);
if (v___x_74_ == 0)
{
lean_object* v___x_75_; uint8_t v___x_76_; 
v___x_75_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_76_ = lp_setka_List_any___at___00Setka_reach_spec__0(v_glue_65_, v_n_73_, v_x_67_, v_x_68_, v___x_75_);
lean_dec(v_n_73_);
return v___x_76_;
}
else
{
lean_dec(v_n_73_);
lean_dec(v_x_68_);
lean_dec_ref(v_glue_65_);
return v___x_74_;
}
}
}
}
LEAN_EXPORT uint8_t lp_setka_List_any___at___00Setka_reach_spec__0(lean_object* v_glue_77_, lean_object* v_n_78_, lean_object* v_x_79_, lean_object* v_x_80_, lean_object* v_x_81_){
_start:
{
if (lean_obj_tag(v_x_81_) == 0)
{
uint8_t v___x_82_; 
lean_dec(v_x_80_);
lean_dec_ref(v_glue_77_);
v___x_82_ = 0;
return v___x_82_;
}
else
{
lean_object* v_head_83_; lean_object* v_tail_84_; uint8_t v___x_85_; 
v_head_83_ = lean_ctor_get(v_x_81_, 0);
lean_inc_n(v_head_83_, 2);
v_tail_84_ = lean_ctor_get(v_x_81_, 1);
lean_inc(v_tail_84_);
lean_dec_ref_known(v_x_81_, 2);
lean_inc_ref(v_glue_77_);
v___x_85_ = lp_setka_Setka_reach(v_glue_77_, v_n_78_, v_x_79_, v_head_83_);
if (v___x_85_ == 0)
{
lean_dec(v_head_83_);
v_x_81_ = v_tail_84_;
goto _start;
}
else
{
uint8_t v___x_87_; 
lean_inc(v_x_80_);
lean_inc_ref(v_glue_77_);
v___x_87_ = lp_setka_Setka_adj(v_glue_77_, v_head_83_, v_x_80_);
if (v___x_87_ == 0)
{
v_x_81_ = v_tail_84_;
goto _start;
}
else
{
lean_dec(v_tail_84_);
lean_dec(v_x_80_);
lean_dec_ref(v_glue_77_);
return v___x_87_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_List_any___at___00Setka_reach_spec__0___boxed(lean_object* v_glue_89_, lean_object* v_n_90_, lean_object* v_x_91_, lean_object* v_x_92_, lean_object* v_x_93_){
_start:
{
uint8_t v_res_94_; lean_object* v_r_95_; 
v_res_94_ = lp_setka_List_any___at___00Setka_reach_spec__0(v_glue_89_, v_n_90_, v_x_91_, v_x_92_, v_x_93_);
lean_dec(v_x_91_);
lean_dec(v_n_90_);
v_r_95_ = lean_box(v_res_94_);
return v_r_95_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_reach___boxed(lean_object* v_glue_96_, lean_object* v_x_97_, lean_object* v_x_98_, lean_object* v_x_99_){
_start:
{
uint8_t v_res_100_; lean_object* v_r_101_; 
v_res_100_ = lp_setka_Setka_reach(v_glue_96_, v_x_97_, v_x_98_, v_x_99_);
lean_dec(v_x_98_);
lean_dec(v_x_97_);
v_r_101_ = lean_box(v_res_100_);
return v_r_101_;
}
}
LEAN_EXPORT uint8_t lp_setka_List_all___at___00Setka_comps_spec__0(lean_object* v_i_102_, uint8_t v___x_103_, lean_object* v_glue_104_, lean_object* v_x_105_){
_start:
{
if (lean_obj_tag(v_x_105_) == 0)
{
uint8_t v___x_106_; 
lean_dec_ref(v_glue_104_);
lean_dec(v_i_102_);
v___x_106_ = 1;
return v___x_106_;
}
else
{
lean_object* v_head_107_; lean_object* v_tail_108_; uint8_t v___y_110_; uint8_t v___x_112_; 
v_head_107_ = lean_ctor_get(v_x_105_, 0);
v_tail_108_ = lean_ctor_get(v_x_105_, 1);
v___x_112_ = lean_nat_dec_lt(v_head_107_, v_i_102_);
if (v___x_112_ == 0)
{
v___y_110_ = v___x_103_;
goto v___jp_109_;
}
else
{
lean_object* v___x_113_; uint8_t v___x_114_; 
v___x_113_ = lean_unsigned_to_nat(4u);
lean_inc(v_i_102_);
lean_inc_ref(v_glue_104_);
v___x_114_ = lp_setka_Setka_reach(v_glue_104_, v___x_113_, v_head_107_, v_i_102_);
if (v___x_114_ == 0)
{
v___y_110_ = v___x_103_;
goto v___jp_109_;
}
else
{
uint8_t v___x_115_; 
lean_dec_ref(v_glue_104_);
lean_dec(v_i_102_);
v___x_115_ = 0;
return v___x_115_;
}
}
v___jp_109_:
{
if (v___y_110_ == 0)
{
lean_dec_ref(v_glue_104_);
lean_dec(v_i_102_);
return v___y_110_;
}
else
{
v_x_105_ = v_tail_108_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_List_all___at___00Setka_comps_spec__0___boxed(lean_object* v_i_116_, lean_object* v___x_117_, lean_object* v_glue_118_, lean_object* v_x_119_){
_start:
{
uint8_t v___x_157__boxed_120_; uint8_t v_res_121_; lean_object* v_r_122_; 
v___x_157__boxed_120_ = lean_unbox(v___x_117_);
v_res_121_ = lp_setka_List_all___at___00Setka_comps_spec__0(v_i_116_, v___x_157__boxed_120_, v_glue_118_, v_x_119_);
lean_dec(v_x_119_);
v_r_122_ = lean_box(v_res_121_);
return v_r_122_;
}
}
LEAN_EXPORT lean_object* lp_setka_List_filterTR_loop___at___00Setka_comps_spec__1(lean_object* v_pres_123_, lean_object* v_glue_124_, lean_object* v_a_125_, lean_object* v_a_126_){
_start:
{
if (lean_obj_tag(v_a_125_) == 0)
{
lean_object* v___x_127_; 
lean_dec_ref(v_glue_124_);
lean_dec_ref(v_pres_123_);
v___x_127_ = l_List_reverse___redArg(v_a_126_);
return v___x_127_;
}
else
{
lean_object* v_head_128_; lean_object* v_tail_129_; lean_object* v___x_131_; uint8_t v_isShared_132_; uint8_t v_isSharedCheck_144_; 
v_head_128_ = lean_ctor_get(v_a_125_, 0);
v_tail_129_ = lean_ctor_get(v_a_125_, 1);
v_isSharedCheck_144_ = !lean_is_exclusive(v_a_125_);
if (v_isSharedCheck_144_ == 0)
{
v___x_131_ = v_a_125_;
v_isShared_132_ = v_isSharedCheck_144_;
goto v_resetjp_130_;
}
else
{
lean_inc(v_tail_129_);
lean_inc(v_head_128_);
lean_dec(v_a_125_);
v___x_131_ = lean_box(0);
v_isShared_132_ = v_isSharedCheck_144_;
goto v_resetjp_130_;
}
v_resetjp_130_:
{
lean_object* v___x_133_; uint8_t v___x_134_; 
lean_inc_ref(v_pres_123_);
lean_inc(v_head_128_);
v___x_133_ = lean_apply_1(v_pres_123_, v_head_128_);
v___x_134_ = lean_unbox(v___x_133_);
if (v___x_134_ == 0)
{
lean_del_object(v___x_131_);
lean_dec(v_head_128_);
v_a_125_ = v_tail_129_;
goto _start;
}
else
{
lean_object* v___x_136_; uint8_t v___x_137_; uint8_t v___x_138_; 
v___x_136_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_137_ = lean_unbox(v___x_133_);
lean_inc_ref(v_glue_124_);
lean_inc(v_head_128_);
v___x_138_ = lp_setka_List_all___at___00Setka_comps_spec__0(v_head_128_, v___x_137_, v_glue_124_, v___x_136_);
if (v___x_138_ == 0)
{
lean_del_object(v___x_131_);
lean_dec(v_head_128_);
v_a_125_ = v_tail_129_;
goto _start;
}
else
{
lean_object* v___x_141_; 
if (v_isShared_132_ == 0)
{
lean_ctor_set(v___x_131_, 1, v_a_126_);
v___x_141_ = v___x_131_;
goto v_reusejp_140_;
}
else
{
lean_object* v_reuseFailAlloc_143_; 
v_reuseFailAlloc_143_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_143_, 0, v_head_128_);
lean_ctor_set(v_reuseFailAlloc_143_, 1, v_a_126_);
v___x_141_ = v_reuseFailAlloc_143_;
goto v_reusejp_140_;
}
v_reusejp_140_:
{
v_a_125_ = v_tail_129_;
v_a_126_ = v___x_141_;
goto _start;
}
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_comps(lean_object* v_pres_145_, lean_object* v_glue_146_){
_start:
{
lean_object* v___x_147_; lean_object* v___x_148_; lean_object* v___x_149_; lean_object* v___x_150_; 
v___x_147_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_148_ = lean_box(0);
v___x_149_ = lp_setka_List_filterTR_loop___at___00Setka_comps_spec__1(v_pres_145_, v_glue_146_, v___x_147_, v___x_148_);
v___x_150_ = l_List_lengthTR___redArg(v___x_149_);
lean_dec(v___x_149_);
return v___x_150_;
}
}
LEAN_EXPORT lean_object* lp_setka_List_filterTR_loop___at___00Setka_kk_spec__0(lean_object* v_pres_151_, lean_object* v_a_152_, lean_object* v_a_153_){
_start:
{
if (lean_obj_tag(v_a_152_) == 0)
{
lean_object* v___x_154_; 
lean_dec_ref(v_pres_151_);
v___x_154_ = l_List_reverse___redArg(v_a_153_);
return v___x_154_;
}
else
{
lean_object* v_head_155_; lean_object* v_tail_156_; lean_object* v___x_158_; uint8_t v_isShared_159_; uint8_t v_isSharedCheck_167_; 
v_head_155_ = lean_ctor_get(v_a_152_, 0);
v_tail_156_ = lean_ctor_get(v_a_152_, 1);
v_isSharedCheck_167_ = !lean_is_exclusive(v_a_152_);
if (v_isSharedCheck_167_ == 0)
{
v___x_158_ = v_a_152_;
v_isShared_159_ = v_isSharedCheck_167_;
goto v_resetjp_157_;
}
else
{
lean_inc(v_tail_156_);
lean_inc(v_head_155_);
lean_dec(v_a_152_);
v___x_158_ = lean_box(0);
v_isShared_159_ = v_isSharedCheck_167_;
goto v_resetjp_157_;
}
v_resetjp_157_:
{
lean_object* v___x_160_; uint8_t v___x_161_; 
lean_inc_ref(v_pres_151_);
lean_inc(v_head_155_);
v___x_160_ = lean_apply_1(v_pres_151_, v_head_155_);
v___x_161_ = lean_unbox(v___x_160_);
if (v___x_161_ == 0)
{
lean_del_object(v___x_158_);
lean_dec(v_head_155_);
v_a_152_ = v_tail_156_;
goto _start;
}
else
{
lean_object* v___x_164_; 
if (v_isShared_159_ == 0)
{
lean_ctor_set(v___x_158_, 1, v_a_153_);
v___x_164_ = v___x_158_;
goto v_reusejp_163_;
}
else
{
lean_object* v_reuseFailAlloc_166_; 
v_reuseFailAlloc_166_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_166_, 0, v_head_155_);
lean_ctor_set(v_reuseFailAlloc_166_, 1, v_a_153_);
v___x_164_ = v_reuseFailAlloc_166_;
goto v_reusejp_163_;
}
v_reusejp_163_:
{
v_a_152_ = v_tail_156_;
v_a_153_ = v___x_164_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_kk(lean_object* v_pres_168_){
_start:
{
lean_object* v___x_169_; lean_object* v___x_170_; lean_object* v___x_171_; lean_object* v___x_172_; 
v___x_169_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_170_ = lean_box(0);
v___x_171_ = lp_setka_List_filterTR_loop___at___00Setka_kk_spec__0(v_pres_168_, v___x_169_, v___x_170_);
v___x_172_ = l_List_lengthTR___redArg(v___x_171_);
lean_dec(v___x_171_);
return v___x_172_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_ss(lean_object* v_glue_173_){
_start:
{
lean_object* v___x_174_; lean_object* v___x_175_; lean_object* v___x_176_; lean_object* v___x_177_; 
v___x_174_ = lean_obj_once(&lp_setka_Setka_valid___closed__0, &lp_setka_Setka_valid___closed__0_once, _init_lp_setka_Setka_valid___closed__0);
v___x_175_ = lean_box(0);
v___x_176_ = lp_setka_List_filterTR_loop___at___00Setka_kk_spec__0(v_glue_173_, v___x_174_, v___x_175_);
v___x_177_ = l_List_lengthTR___redArg(v___x_176_);
lean_dec(v___x_176_);
return v___x_177_;
}
}
LEAN_EXPORT uint8_t lp_setka_Setka_bits(lean_object* v_m_178_, lean_object* v_i_179_){
_start:
{
uint8_t v___x_180_; 
v___x_180_ = l_Nat_testBit(v_m_178_, v_i_179_);
return v___x_180_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_bits___boxed(lean_object* v_m_181_, lean_object* v_i_182_){
_start:
{
uint8_t v_res_183_; lean_object* v_r_184_; 
v_res_183_ = lp_setka_Setka_bits(v_m_181_, v_i_182_);
lean_dec(v_i_182_);
lean_dec(v_m_181_);
v_r_184_ = lean_box(v_res_183_);
return v_r_184_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_dd(lean_object* v_b0_185_, lean_object* v_O_186_, lean_object* v_S_187_, lean_object* v_q_188_){
_start:
{
lean_object* v___x_189_; lean_object* v___x_190_; lean_object* v___x_191_; 
v___x_189_ = lean_int_sub(v_b0_185_, v_O_186_);
v___x_190_ = lean_int_add(v___x_189_, v_S_187_);
lean_dec(v___x_189_);
v___x_191_ = lean_int_sub(v___x_190_, v_q_188_);
lean_dec(v___x_190_);
return v___x_191_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_dd___boxed(lean_object* v_b0_192_, lean_object* v_O_193_, lean_object* v_S_194_, lean_object* v_q_195_){
_start:
{
lean_object* v_res_196_; 
v_res_196_ = lp_setka_Setka_dd(v_b0_192_, v_O_193_, v_S_194_, v_q_195_);
lean_dec(v_q_195_);
lean_dec(v_S_194_);
lean_dec(v_O_193_);
lean_dec(v_b0_192_);
return v_res_196_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorIdx___impl(lean_object* v_x_197_){
_start:
{
lean_object* v___x_198_; 
v___x_198_ = lean_obj_tag_nat(v_x_197_);
return v___x_198_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorIdx___impl___boxed(lean_object* v_x_199_){
_start:
{
lean_object* v_res_200_; 
v_res_200_ = lp_setka_Setka_Step_ctorIdx___impl(v_x_199_);
lean_dec(v_x_199_);
return v_res_200_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim___redArg(lean_object* v_t_201_, lean_object* v_k_202_){
_start:
{
if (lean_obj_tag(v_t_201_) == 0)
{
return v_k_202_;
}
else
{
lean_object* v_00_u03b4_203_; lean_object* v___x_204_; 
v_00_u03b4_203_ = lean_ctor_get(v_t_201_, 0);
lean_inc(v_00_u03b4_203_);
lean_dec_ref_known(v_t_201_, 1);
v___x_204_ = lean_apply_1(v_k_202_, v_00_u03b4_203_);
return v___x_204_;
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim(lean_object* v_motive_205_, lean_object* v_ctorIdx_206_, lean_object* v_t_207_, lean_object* v_h_208_, lean_object* v_k_209_){
_start:
{
lean_object* v___x_210_; 
v___x_210_ = lp_setka_Setka_Step_ctorElim___redArg(v_t_207_, v_k_209_);
return v___x_210_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_ctorElim___boxed(lean_object* v_motive_211_, lean_object* v_ctorIdx_212_, lean_object* v_t_213_, lean_object* v_h_214_, lean_object* v_k_215_){
_start:
{
lean_object* v_res_216_; 
v_res_216_ = lp_setka_Setka_Step_ctorElim(v_motive_211_, v_ctorIdx_212_, v_t_213_, v_h_214_, v_k_215_);
lean_dec(v_ctorIdx_212_);
return v_res_216_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_stretch_elim___redArg(lean_object* v_t_217_, lean_object* v_stretch_218_){
_start:
{
lean_object* v___x_219_; 
v___x_219_ = lp_setka_Setka_Step_ctorElim___redArg(v_t_217_, v_stretch_218_);
return v___x_219_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_stretch_elim(lean_object* v_motive_220_, lean_object* v_t_221_, lean_object* v_h_222_, lean_object* v_stretch_223_){
_start:
{
lean_object* v___x_224_; 
v___x_224_ = lp_setka_Setka_Step_ctorElim___redArg(v_t_221_, v_stretch_223_);
return v___x_224_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_glue_elim___redArg(lean_object* v_t_225_, lean_object* v_glue_226_){
_start:
{
lean_object* v___x_227_; 
v___x_227_ = lp_setka_Setka_Step_ctorElim___redArg(v_t_225_, v_glue_226_);
return v___x_227_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_Step_glue_elim(lean_object* v_motive_228_, lean_object* v_t_229_, lean_object* v_h_230_, lean_object* v_glue_231_){
_start:
{
lean_object* v___x_232_; 
v___x_232_ = lp_setka_Setka_Step_ctorElim___redArg(v_t_229_, v_glue_231_);
return v___x_232_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_run(lean_object* v_x_233_, lean_object* v_x_234_){
_start:
{
if (lean_obj_tag(v_x_234_) == 0)
{
return v_x_233_;
}
else
{
lean_object* v_head_235_; 
v_head_235_ = lean_ctor_get(v_x_234_, 0);
if (lean_obj_tag(v_head_235_) == 0)
{
lean_object* v_tail_236_; 
v_tail_236_ = lean_ctor_get(v_x_234_, 1);
v_x_234_ = v_tail_236_;
goto _start;
}
else
{
lean_object* v_tail_238_; lean_object* v_00_u03b4_239_; lean_object* v___x_240_; 
v_tail_238_ = lean_ctor_get(v_x_234_, 1);
v_00_u03b4_239_ = lean_ctor_get(v_head_235_, 0);
v___x_240_ = lean_int_add(v_x_233_, v_00_u03b4_239_);
lean_dec(v_x_233_);
v_x_233_ = v___x_240_;
v_x_234_ = v_tail_238_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_run___boxed(lean_object* v_x_242_, lean_object* v_x_243_){
_start:
{
lean_object* v_res_244_; 
v_res_244_ = lp_setka_Setka_run(v_x_242_, v_x_243_);
lean_dec(v_x_243_);
return v_res_244_;
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_glues(lean_object* v_x_245_){
_start:
{
if (lean_obj_tag(v_x_245_) == 0)
{
lean_object* v___x_246_; 
v___x_246_ = lean_unsigned_to_nat(0u);
return v___x_246_;
}
else
{
lean_object* v_head_247_; 
v_head_247_ = lean_ctor_get(v_x_245_, 0);
if (lean_obj_tag(v_head_247_) == 0)
{
lean_object* v_tail_248_; 
v_tail_248_ = lean_ctor_get(v_x_245_, 1);
v_x_245_ = v_tail_248_;
goto _start;
}
else
{
lean_object* v_tail_250_; lean_object* v___x_251_; lean_object* v___x_252_; lean_object* v___x_253_; 
v_tail_250_ = lean_ctor_get(v_x_245_, 1);
v___x_251_ = lp_setka_Setka_glues(v_tail_250_);
v___x_252_ = lean_unsigned_to_nat(1u);
v___x_253_ = lean_nat_add(v___x_251_, v___x_252_);
lean_dec(v___x_251_);
return v___x_253_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka_Setka_glues___boxed(lean_object* v_x_254_){
_start:
{
lean_object* v_res_255_; 
v_res_255_ = lp_setka_Setka_glues(v_x_254_);
lean_dec(v_x_254_);
return v_res_255_;
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_run_match__1_splitter___redArg(lean_object* v_x_256_, lean_object* v_x_257_, lean_object* v_h__1_258_, lean_object* v_h__2_259_, lean_object* v_h__3_260_){
_start:
{
if (lean_obj_tag(v_x_257_) == 0)
{
lean_object* v___x_261_; 
lean_dec(v_h__3_260_);
lean_dec(v_h__2_259_);
v___x_261_ = lean_apply_1(v_h__1_258_, v_x_256_);
return v___x_261_;
}
else
{
lean_object* v_head_262_; 
lean_dec(v_h__1_258_);
v_head_262_ = lean_ctor_get(v_x_257_, 0);
if (lean_obj_tag(v_head_262_) == 0)
{
lean_object* v_tail_263_; lean_object* v___x_264_; 
lean_dec(v_h__3_260_);
v_tail_263_ = lean_ctor_get(v_x_257_, 1);
lean_inc(v_tail_263_);
lean_dec_ref_known(v_x_257_, 2);
v___x_264_ = lean_apply_2(v_h__2_259_, v_x_256_, v_tail_263_);
return v___x_264_;
}
else
{
lean_object* v_tail_265_; lean_object* v_00_u03b4_266_; lean_object* v___x_267_; 
lean_inc_ref(v_head_262_);
lean_dec(v_h__2_259_);
v_tail_265_ = lean_ctor_get(v_x_257_, 1);
lean_inc(v_tail_265_);
lean_dec_ref_known(v_x_257_, 2);
v_00_u03b4_266_ = lean_ctor_get(v_head_262_, 0);
lean_inc(v_00_u03b4_266_);
lean_dec_ref_known(v_head_262_, 1);
v___x_267_ = lean_apply_3(v_h__3_260_, v_x_256_, v_00_u03b4_266_, v_tail_265_);
return v___x_267_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_run_match__1_splitter(lean_object* v_motive_268_, lean_object* v_x_269_, lean_object* v_x_270_, lean_object* v_h__1_271_, lean_object* v_h__2_272_, lean_object* v_h__3_273_){
_start:
{
if (lean_obj_tag(v_x_270_) == 0)
{
lean_object* v___x_274_; 
lean_dec(v_h__3_273_);
lean_dec(v_h__2_272_);
v___x_274_ = lean_apply_1(v_h__1_271_, v_x_269_);
return v___x_274_;
}
else
{
lean_object* v_head_275_; 
lean_dec(v_h__1_271_);
v_head_275_ = lean_ctor_get(v_x_270_, 0);
if (lean_obj_tag(v_head_275_) == 0)
{
lean_object* v_tail_276_; lean_object* v___x_277_; 
lean_dec(v_h__3_273_);
v_tail_276_ = lean_ctor_get(v_x_270_, 1);
lean_inc(v_tail_276_);
lean_dec_ref_known(v_x_270_, 2);
v___x_277_ = lean_apply_2(v_h__2_272_, v_x_269_, v_tail_276_);
return v___x_277_;
}
else
{
lean_object* v_tail_278_; lean_object* v_00_u03b4_279_; lean_object* v___x_280_; 
lean_inc_ref(v_head_275_);
lean_dec(v_h__2_272_);
v_tail_278_ = lean_ctor_get(v_x_270_, 1);
lean_inc(v_tail_278_);
lean_dec_ref_known(v_x_270_, 2);
v_00_u03b4_279_ = lean_ctor_get(v_head_275_, 0);
lean_inc(v_00_u03b4_279_);
lean_dec_ref_known(v_head_275_, 1);
v___x_280_ = lean_apply_3(v_h__3_273_, v_x_269_, v_00_u03b4_279_, v_tail_278_);
return v___x_280_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_glues_match__1_splitter___redArg(lean_object* v_x_281_, lean_object* v_h__1_282_, lean_object* v_h__2_283_, lean_object* v_h__3_284_){
_start:
{
if (lean_obj_tag(v_x_281_) == 0)
{
lean_object* v___x_285_; lean_object* v___x_286_; 
lean_dec(v_h__3_284_);
lean_dec(v_h__2_283_);
v___x_285_ = lean_box(0);
v___x_286_ = lean_apply_1(v_h__1_282_, v___x_285_);
return v___x_286_;
}
else
{
lean_object* v_head_287_; 
lean_dec(v_h__1_282_);
v_head_287_ = lean_ctor_get(v_x_281_, 0);
if (lean_obj_tag(v_head_287_) == 0)
{
lean_object* v_tail_288_; lean_object* v___x_289_; 
lean_dec(v_h__3_284_);
v_tail_288_ = lean_ctor_get(v_x_281_, 1);
lean_inc(v_tail_288_);
lean_dec_ref_known(v_x_281_, 2);
v___x_289_ = lean_apply_1(v_h__2_283_, v_tail_288_);
return v___x_289_;
}
else
{
lean_object* v_tail_290_; lean_object* v_00_u03b4_291_; lean_object* v___x_292_; 
lean_inc_ref(v_head_287_);
lean_dec(v_h__2_283_);
v_tail_290_ = lean_ctor_get(v_x_281_, 1);
lean_inc(v_tail_290_);
lean_dec_ref_known(v_x_281_, 2);
v_00_u03b4_291_ = lean_ctor_get(v_head_287_, 0);
lean_inc(v_00_u03b4_291_);
lean_dec_ref_known(v_head_287_, 1);
v___x_292_ = lean_apply_2(v_h__3_284_, v_00_u03b4_291_, v_tail_290_);
return v___x_292_;
}
}
}
}
LEAN_EXPORT lean_object* lp_setka___private_Setka_Glue_0__Setka_glues_match__1_splitter(lean_object* v_motive_293_, lean_object* v_x_294_, lean_object* v_h__1_295_, lean_object* v_h__2_296_, lean_object* v_h__3_297_){
_start:
{
if (lean_obj_tag(v_x_294_) == 0)
{
lean_object* v___x_298_; lean_object* v___x_299_; 
lean_dec(v_h__3_297_);
lean_dec(v_h__2_296_);
v___x_298_ = lean_box(0);
v___x_299_ = lean_apply_1(v_h__1_295_, v___x_298_);
return v___x_299_;
}
else
{
lean_object* v_head_300_; 
lean_dec(v_h__1_295_);
v_head_300_ = lean_ctor_get(v_x_294_, 0);
if (lean_obj_tag(v_head_300_) == 0)
{
lean_object* v_tail_301_; lean_object* v___x_302_; 
lean_dec(v_h__3_297_);
v_tail_301_ = lean_ctor_get(v_x_294_, 1);
lean_inc(v_tail_301_);
lean_dec_ref_known(v_x_294_, 2);
v___x_302_ = lean_apply_1(v_h__2_296_, v_tail_301_);
return v___x_302_;
}
else
{
lean_object* v_tail_303_; lean_object* v_00_u03b4_304_; lean_object* v___x_305_; 
lean_inc_ref(v_head_300_);
lean_dec(v_h__2_296_);
v_tail_303_ = lean_ctor_get(v_x_294_, 1);
lean_inc(v_tail_303_);
lean_dec_ref_known(v_x_294_, 2);
v_00_u03b4_304_ = lean_ctor_get(v_head_300_, 0);
lean_inc(v_00_u03b4_304_);
lean_dec_ref_known(v_head_300_, 1);
v___x_305_ = lean_apply_2(v_h__3_297_, v_00_u03b4_304_, v_tail_303_);
return v___x_305_;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
void lean_initialize_runtime_module();
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_setka_Setka_Glue(uint8_t builtin) {
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
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
