if (intrinsicID == llvm::Intrinsic::abs) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::AbsOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::bitreverse) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::BitReverseOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::copysign) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CopySignOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_align) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroAlignOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_begin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroBeginOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_end) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroEndOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_free) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroFreeOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_id) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroIdOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_resume) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroResumeOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_save) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroSaveOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_size) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroSizeOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::coro_suspend) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CoroSuspendOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::cos) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CosOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::ctlz) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CountLeadingZerosOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::cttz) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CountTrailingZerosOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::ctpop) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::CtPopOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::eh_typeid_for) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::EhTypeidForOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::exp2) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::Exp2Op>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::exp) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::ExpOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::fabs) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FAbsOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::ceil) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FCeilOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::floor) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FFloorOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::fma) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FMAOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::fmuladd) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FMulAddOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::trunc) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::FTruncOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::get_active_lane_mask) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::GetActiveLaneMaskOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::lifetime_end) {

    odsBuilder.create<LLVM::LifetimeEndOp>(
      translateLoc(callInst->getDebugLoc()), matchIntegerAttr(processValue(callInst->getArgOperand(0))), processValue(callInst->getArgOperand(1)));
  
  return success();
}
if (intrinsicID == llvm::Intrinsic::lifetime_start) {

    odsBuilder.create<LLVM::LifetimeStartOp>(
      translateLoc(callInst->getDebugLoc()), matchIntegerAttr(processValue(callInst->getArgOperand(0))), processValue(callInst->getArgOperand(1)));
  
  return success();
}
if (intrinsicID == llvm::Intrinsic::log10) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::Log10Op>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::log2) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::Log2Op>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::log) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::LogOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::maxnum) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::MaxNumOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::maximum) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::MaximumOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::memcpy_inline) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::MemcpyInlineOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::memcpy) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::MemcpyOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::memmove) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::MemmoveOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::memset) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::MemsetOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::minnum) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::MinNumOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::minimum) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::MinimumOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::powi) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::PowIOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::pow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::PowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::prefetch) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::Prefetch>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::roundeven) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::RoundEvenOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::round) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::RoundOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::sadd_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SAddWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::smax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SMaxOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::smin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::smul_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SMulWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::ssub_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SSubWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::sin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::sqrt) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::SqrtOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::stackrestore) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::StackRestoreOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::stacksave) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::StackSaveOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::experimental_stepvector) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::StepVectorOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::uadd_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::UAddWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::umax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::UMaxOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::umin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::UMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::umul_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::UMulWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::usub_with_overflow) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::USubWithOverflowOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_ashr) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPAShrOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_add) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPAddOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_and) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPAndOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fadd) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFAddOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fdiv) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFDivOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fmul) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFMulOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fneg) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFNegOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fpext) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFPExtOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fptosi) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFPToSIOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fptoui) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFPToUIOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fptrunc) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFPTruncOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_frem) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFRemOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fsub) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFSubOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_fma) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPFmaOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_inttoptr) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPIntToPtrOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_lshr) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPLShrOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_load) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPLoadOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_merge) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPMergeMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_mul) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPMulOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_or) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPOrOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_ptrtoint) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPPtrToIntOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_add) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceAddOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_and) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceAndOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_fadd) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceFAddOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_fmax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceFMaxOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_fmin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceFMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_fmul) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceFMulOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_mul) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceMulOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_or) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceOrOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_smax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceSMaxOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_smin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceSMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_umax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceUMaxOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_umin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceUMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_reduce_xor) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPReduceXorOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_sdiv) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSDivOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_sext) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSExtOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_sitofp) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSIToFPOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_srem) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSRemOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_select) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSelectMinOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_shl) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPShlOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_store) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPStoreOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::experimental_vp_strided_load) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPStridedLoadOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::experimental_vp_strided_store) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPStridedStoreOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_sub) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPSubOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_trunc) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPTruncOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_udiv) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPUDivOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_uitofp) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPUIToFPOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_urem) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPURemOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_xor) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPXorOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vp_zext) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::VPZExtOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vacopy) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::VaCopyOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::vaend) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::VaEndOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::vastart) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::VaStartOp>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::masked_compressstore) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {};
    Operation *op = odsBuilder.create<::mlir::LLVM::masked_compressstore>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    (void)op;
  return success();
}
if (intrinsicID == llvm::Intrinsic::masked_expandload) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::masked_expandload>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_add) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_add>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_and) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_and>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_fmax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_fmax>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_fmin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_fmin>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_mul) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_mul>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_or) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_or>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_smax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_smax>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_smin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_smin>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_umax) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_umax>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_umin) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_umin>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vector_reduce_xor) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vector_reduce_xor>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
if (intrinsicID == llvm::Intrinsic::vscale) {

    SmallVector<llvm::Value *> operands(callInst->args());
    SmallVector<Type> resultTypes =
    {convertType(callInst->getType())};
    Operation *op = odsBuilder.create<::mlir::LLVM::vscale>(
      translateLoc(callInst->getDebugLoc()),
      resultTypes,
      processValues(operands));
    instMap[callInst] = op->getResult(0);
  return success();
}
